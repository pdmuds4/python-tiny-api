from ..._abstruct import UseCaseModel
from ..service import TakeScreenShotService, SendMessageService
from ..dto import SendLiveScheduleRequestDTO


class SendLiveScheduleUseCase(UseCaseModel):
    request: SendLiveScheduleRequestDTO
    takeScreenShotService: TakeScreenShotService
    sendMessageService: SendMessageService

    def __init__(self, 
        request: SendLiveScheduleRequestDTO,
        takeScreenShotService: TakeScreenShotService,
        sendMessageService: SendMessageService
    ):
        self.request = request
        self.takeScreenShotService = takeScreenShotService
        self.sendMessageService = sendMessageService


    def execute(self) -> SendLiveScheduleRequestDTO:
        schedule_url = self.request.schedule_url

        screen_shot_binary = self.takeScreenShotService.execute(schedule_url)
        
        send_message_request = {
            "data": {
                "content": "@everyone \n今週の配信予定をお届けしますニャ！<:nico_nya:1390291846084952205><:nico_nya:1390291846084952205><:nico_nya:1390291846084952205>"
            },
            "files": {
                "file": ("image.png", screen_shot_binary, "image/png")
            }
        }
        
        self.sendMessageService.execute(send_message_request)