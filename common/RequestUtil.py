import requests


class RequestUtil:

    def send_post(self, url, data):

        try:

            response = requests.post(
                url=url,
                json=data,
                timeout=10
            )

            return response

        except Exception as e:

            print("请求异常:", e)

            return None