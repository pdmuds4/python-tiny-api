import sys, os, socketio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse


router = APIRouter()
sio = socketio.AsyncServer(
    cors_allowed_origins=[],
    async_mode='asgi'
)

socket_app = socketio.ASGIApp(sio)


@router.get("/mhjoinup", tags=["mh-joinup"])
async def mhjoinup():
    return JSONResponse({ "message": "This is /mhjoinup router!" })


@sio.on('connect')
async def socket_connect(sid, env):
    print(f"Client {sid} connected")


@sio.on('disconnect')
async def socket_disconnect(sid):
    print(f"Client {sid} disconnected")