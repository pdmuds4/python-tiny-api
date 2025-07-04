import requests, json, os

from ..._abstruct import ServiceModel
from ..._error import UseCaseError
from ..valueObject import ScheduleURL


class TakeScreenShotService(ServiceModel):
    def execute(self, request: ScheduleURL) -> str:
        response = requests.post(
            f'https://production-sfo.browserless.io/screenshot?token={os.getenv("BLOWSER_LESS_API_KEY")}',
            data = json.dumps({
                "url": request.value,
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
                "waitForTimeout": 10000
            }),
            headers = {
                'Content-Type': 'application/json'
            }
        )
            
        if (response.status_code != 200):
            raise UseCaseError(
                message="Browserless.ioのリクエストに失敗しました",
                detail=response.reason,
                status_code=response.status_code
            )

        return response.content
