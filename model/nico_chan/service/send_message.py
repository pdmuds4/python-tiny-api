import requests, json, os

from ..._abstruct import ServiceModel
from ..._error import UseCaseError


class SendMessageService(ServiceModel):
    def execute(self, request: dict) -> None:
        response = requests.post(
            os.getenv("DISCORD_WEBHOOK_NICOCHAN_URI"), 
            data = request["data"],
            files = request["files"]
        )

        if (response.status_code != 204):
            raise UseCaseError(
                message="DiscordWebhookのリクエストに失敗しました。",
                detail=response.reason,
                status_code=response.status_code
            )