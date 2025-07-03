import sys, os, requests, json, dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/nico-chan")
dotenv.load_dotenv()


@router.get('/send-live-schedule', tags=['discord-bot-webhook', 'nico-chan'])
async def send_live_schedule(request):
    pass