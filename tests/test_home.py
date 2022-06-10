import requests

def test_home():
    r = requests.get("http://127.0.0.1:5002?a=3&b=1") 
    assert r.status_code == 200
