import sys, os, socketio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter
from fastapi.responses import JSONResponse

from model._error import BaseError

from model.mhjoinup.dto import *
from model.mhjoinup.payload import *

from model.mhjoinup.valueObject import *
from model.mhjoinup.usecase import *

router = APIRouter()
sio = socketio.AsyncServer(
    cors_allowed_origins=[],
    async_mode='asgi'
)

socket_app = socketio.ASGIApp(sio)


@router.get("/mhjoinup", tags=["mh-joinup"])
async def mhjoinup():
    return JSONResponse({ "message": "This is /mhjoinup router!" })


@router.post("/mhjoinup/emit_webhook", tags=["mh-joinup"], response_model=EmitWebhookResponsePayload)
async def emit_webhook(request: EmitWebhookRequestPayload):
    try:
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

        await sio.emit(request.videoId, response_payload.model_dump())

        return response_payload
    except Exception as e:
        if isinstance(e, BaseError):
            return JSONResponse(
                status_code=e.status_code,
                content={
                    "message": e.message,
                    "detail": e.detail,
                    "level": e.level
                }
            )
        else:
            return JSONResponse(
                status_code=500,
                content={
                    "message": "An unexpected error occurred.",
                    "detail": str(e),
                    "level": "unknown"
                }
            )



@sio.on('connect')
async def socket_connect(sid, env):
    print(f"Client {sid} connected")


@sio.on('disconnect')
async def socket_disconnect(sid):
    print(f"Client {sid} disconnected")