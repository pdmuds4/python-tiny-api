import sys, os, requests, json, dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/nico-chan")
dotenv.load_dotenv()


@router.get('/send', tags=['discord-bot-webhook', 'nico-chan'])
async def send():
    message = {
        "avatar_url": 'https://yt3.googleusercontent.com/MwHajCaVvW5GN0HUf2WSyfkKEj7LgA0vUXyKumvol66syf8uXQVAD8d4KuN-bp9J2S_shJ9Myww=s160-c-k-c0x00ffffff-no-rj',
        "embeds": [{
            "title": "あいうろ",
            "description": "今週の配信予定をお届けします",
        }]
    }

    response = requests.post(
        os.getenv("DISCORD_WEBHOOK_NICOCHAN_URI"), 
        data=json.dumps(message),
        headers={
            'Content-Type': 'application/json'
        }
    )
    
    return JSONResponse({
        "message": "Send message successful",
        "status": response.status_code
    })