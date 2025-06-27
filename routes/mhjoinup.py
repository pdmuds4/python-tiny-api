import sys, os, socketio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter, Path
from fastapi.responses import JSONResponse

from model.mhjoinup.dto import *
from model.mhjoinup.payload import *

from model.mhjoinup.valueObject import *
from model.mhjoinup.usecase import *

router = APIRouter()
sio = socketio.AsyncServer(
    cors_allowed_origins=[],
    async_mode='asgi'
)

socket_app = socketio.ASGIApp(sio, socketio_path="/socket.io/mhjoinup")


@router.get("/mhjoinup", tags=["mh-joinup"])
async def mhjoinup():
    return JSONResponse({ "message": "This is /mhjoinup router!" })


@router.post("/mhjoinup/emit_webhook", tags=["mh-joinup"], response_model=EmitWebhookResponsePayload)
async def emit_webhook(request: EmitWebhookRequestPayload):
    request_dto = EmitWebhookRequestDTO(
        videoId=YoutubeId(value=request.videoId),
        chatMessages=[
            ChatMessageEntity(
                displayMessage=Message(value=chat_message.displayMessage),
                displayName=UserName(value=chat_message.displayName),
                photoUrl=UserAvatar(value=chat_message.photoUrl),
                platformAudienceId=ChannelId(value=chat_message.platformAudienceId)
            ) for chat_message in request.chatMessages
        ]
    )

    emitWebhookUseCase = EmitWebhookUseCase(request=request_dto)
    response = emitWebhookUseCase.execute()

    response_payload = EmitWebhookResponsePayload(
        youtube_id=response.youtube_id.value,
        chat_data=[
            ChatDataEntityTypes(
                message=chat_data.message.value,
                name=chat_data.name.value,
                avatar=chat_data.avatar.value,
                channel_id=chat_data.channel_id.value
            ) for chat_data in response.chat_data
        ]
    )

    await sio.emit(
        request.videoId,
        response_payload.model_dump(),
        namespace='/castcraft_webhook'
    )

    return response_payload


@router.post("/mhjoinup/emit_management/{user_id}", tags=["mh-joinup"], response_model=EmitManagementPayload)
async def emit_management(
    user_id: str = Path(...), 
    request: EmitManagementPayload = ...
):
    request_dto = EmitManagementDTO(
        user_id=UserId(value=user_id),
        joiner=[ManageInstantEntity(
            name=UserName(value=j.name), 
            avatar=UserAvatar(value=j.avatar), 
            quest=UserQuest(value=j.quest)
        ) for j in request.joiner],
        waiter=[ManageInstantEntity(
            name=UserName(value=w.name), 
            avatar=UserAvatar(value=w.avatar),
            quest=UserQuest(value=w.quest)
        ) for w in request.waiter],
    )

    response_payload = EmitManagementPayload(
        joiner=[{k: v["value"] for [k, v] in j.model_dump().items()} for j in request_dto.joiner],
        waiter=[{k: v["value"] for [k, v] in w.model_dump().items()} for w in request_dto.waiter]
    )

    await sio.emit(
        user_id,
        response_payload,
        namespace='/board_management'
    )
    
    return response_payload


@sio.on('connect', namespace='/castcraft_webhook')
async def socket_castcraft_webhook_connect(sid, env):
    print(f"Client {sid} namespace='/castcraft_webhook' connected")

@sio.on('connect', namespace='/board_management')
async def socket_board_management_connect(sid, env):
    print(f"Client {sid} namespace='/board_management' connected")


@sio.on('disconnect', namespace='*')
async def socket_disconnect(sid):
    print(f"Client {sid} disconnected")