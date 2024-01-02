import requests

ENDPOINT = 'https://reqres.in/api/'
USER = 'users/2'


def test_get_user_successful():
        response = requests.get(ENDPOINT + USER)
        response_body = response.json()
        print(response_body)
        assert response.status_code == 200


def test_header():
    response = requests.get(ENDPOINT + USER)
    print(response.json())
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"


def test_response():
    response = requests.get(ENDPOINT + USER)
    response_body = response.json()
    print(response_body)
    assert response_body["data"]["id"] == 2
    assert response_body["data"]["first_name"] == "Janet"
    assert response_body["data"]["last_name"] == "Weaver"
