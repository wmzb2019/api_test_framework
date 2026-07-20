from common.request_util01 import RequestUtil
import requests

def test_httpbin_get():
    r=requests.get("https://httpbin.org/get")


    print(r.status_code)
    print(r.text)
    assert r.status_code==200

