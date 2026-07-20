import requests

class RequestUtil01:
    def send_post(self,url,data):
        response = requests.post(
            url=url,
            json=data,
            timeout=10
        )
        return response
