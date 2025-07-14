import requests, json
from model._error import ClientError

class BrowserlessClient:
    __apiKey: str

    def __init__(self, apiKey: str):
        self.__apiKey = apiKey

    def screenShot(self, url: str, **kwargs) -> bytes:
        request_url = f'https://production-sfo.browserless.io/screenshot?token={self.__apiKey}'
        request_body = json.dumps({
            "url": url,
            **kwargs
        })

        response = requests.post(
            request_url,
            headers={
                'Content-Type': 'application/json'
            },
            data=request_body
        )

        response_content = response.content

        if not response.ok:
            raise ClientError(
                '[BrowserlessClient] スクリーンショットの取得に失敗しました。',
                response_content.decode(),
                response.status_code
            )
        
        return response_content

