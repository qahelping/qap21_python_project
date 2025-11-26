import requests


def test_main():
    request_get = requests.get("https://httpbin.org/get")
    assert request_get.text
    request_get = requests.request("GET", "https://httpbin.org/get")
    assert request_get.text


def test_main_500():
    url = "https://httpbin.org/status/500"
    r = requests.get(url)

    try:
        r.raise_for_status()
        print("Запрос успешен.")
    except requests.exceptions.HTTPError as err:
        print(f"Ошибка HTTP: {err}")


def test_main_2():
    r = requests.get("https://api.thecatapi.com/v1/images/search?limit=5")
    r.raise_for_status()
    response_json = r.json()

    assert r.status_code == requests.codes.ok

    print(response_json)
    print(response_json[0]["id"])
    print(response_json[0]["url"])

    for item in response_json:
        assert item["id"] != ""
        assert "https://cdn2.thecatapi.com/" in item["url"]
        assert isinstance(item["width"], int)
        assert isinstance(item["height"], int)

        assert item["width"] > 0
        assert item["height"] > 0
