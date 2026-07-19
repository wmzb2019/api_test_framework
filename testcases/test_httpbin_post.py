from common.request_util import RequestUtil


def test_httpbin_post():
    url= "https://httpbin.org/post"
    data = {
        "username":"test001",
        "password":"123456"
    }
    request = RequestUtil()
    response =request.send_post(url,data)
    print(response.status_code)
    assert response.status_code==503

