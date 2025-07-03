import sys, os, requests, json, dotenv
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from fastapi import APIRouter

from model.nico_chan.valueObject import *
from model.nico_chan.service import *
from model.nico_chan.usecase import *

from model.nico_chan.dto import *
from model.nico_chan.payload import *


router = APIRouter(prefix="/nico-chan")
dotenv.load_dotenv()


takeScreenShotService = TakeScreenShotService()
sendMessageService = SendMessageService()


@router.post('/send-live-schedule', tags=['nico-chan'])
async def send_live_schedule(request: SendLiveScheduleRequestPayload):
    request_dto = SendLiveScheduleRequestDTO(
        schedule_url=ScheduleURL(value=request.schedule_url)
    )

    usecase = SendLiveScheduleUseCase(
        request_dto,
        takeScreenShotService,
        sendMessageService
    )

    usecase.execute()