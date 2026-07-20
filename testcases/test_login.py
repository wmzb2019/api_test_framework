from common.request_util import RequestUtil


def test_login_success():

    url = "http://127.0.0.1:5000/login"


    data = {
        "username": "test001",
        "password": "123456"
    }


    request = RequestUtil()


    response = request.send_post(
        url,
        data
    )


    print(response.json())


    assert response.json()["code"] == 0

    assert response.json()["msg"] == "success"