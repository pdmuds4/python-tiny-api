import sys, os, requests, json, dotenv, io
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(prefix="/nico-chan")
dotenv.load_dotenv()


@router.get('/send-live-schedule', tags=['discord-bot-webhook', 'nico-chan'])
async def send_live_schedule():
    browserless_response = requests.post(
        f'https://production-sfo.browserless.io/screenshot?token=2Sbxwgp2AED8sGP0d1527fb70b86502d48fa627d357a8ed8e',
        data = json.dumps({
            "url": "https://mh-joinup.vercel.app/schedule-source?calendar_id=435dd9e81809e2a470643e4627e70eb8c0b60cc21cdb6f2ef95c038c5171538a@group.calendar.google.com&channel_id=UC6pZ4QAQqHrRMd3hr7kH3sg",
            "viewport": {
                "width": 800,
                "height": 545,
                "deviceScaleFactor": 1
            },
            "options": {
                "type": "png"
            },
            "gotoOptions": {
                "waitUntil": "networkidle2"
            },
        }),
        headers = {
            'Content-Type': 'application/json'
        }
    )

    message = {
        "avatar_url": 'https://yt3.googleusercontent.com/MwHajCaVvW5GN0HUf2WSyfkKEj7LgA0vUXyKumvol66syf8uXQVAD8d4KuN-bp9J2S_shJ9Myww=s160-c-k-c0x00ffffff-no-rj',
        "content": "画像やで"
    }

    files = {
        "file": ("image.png", browserless_response.content, "image/png")
    }

    discord_webhook_response = requests.post(
        os.getenv("DISCORD_WEBHOOK_NICOCHAN_URI"), 
        data=message,
        files=files
    )
    
    return JSONResponse({
        "message": "Send message successful",
        "status": discord_webhook_response.status_code
    })