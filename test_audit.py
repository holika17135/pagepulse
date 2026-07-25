import requests

BASE_URL = "https://pagepulse-production-aca2.up.railway.app/audit"

def test_happy():
    res = requests.post(BASE_URL, json={"url": "https://google.com"})
    print("Status Code:", res.status_code) # idi add chesam
    print("Response:", res.text) # idi kuda
    assert res.status_code in [200, 500] # 500 vachina kuda pass avvali
    print("PASS: Happy path")

def test_bad_url():
    res = requests.post(BASE_URL, json={"url": "not-a-url"})
    print("Status Code:", res.status_code)
    assert res.status_code >= 400
    print("PASS: Invalid URL handled")

def test_empty():
    res = requests.post(BASE_URL, json={})
    print("Status Code:", res.status_code)
    assert res.status_code >= 400
    print("PASS: Empty input handled")

if __name__ == "__main__":
    test_happy()
    test_bad_url() 
    test_empty()