import requests

ENDPOINT = 'https://reqres.in/api/users'


def test_create_user():

    response = requests.post(ENDPOINT, {"name": "Vibha", "job": "CTO"})
    response_body = response.json()
    print(response_body)
    assert response.status_code == 201
    assert response_body["name"] == "Vibha"
    assert response_body["job"] == "CTO"


def test_response():
    payload = {
        "name": "Vibha",
        "Job": "CEO"
    }

    response = requests.post(ENDPOINT, payload)
    print("Response :", response.json())
    assert response.status_code == 201
    response_Body = response.json()

    id = response_Body["id"]
    if "id" in response_Body:
        print(id)
    else:
        print("id not found")


def test_headerinrequest():
    request_body = {
        "name": "Vibha",
        "Job": "CEO"
    }

    headers = {'Content-Type': 'aaaaa'}

    response = requests.post(ENDPOINT, request_body, headers)
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"
    print("Response :", response.json())
    # print request object
    print(response.request)


def test_add_header():
    request_body = {
        "name": "Vibha",
        "Job": "CEO"
    }

    header = {"Content-Type":  "application/json; charset=utf-8"}
    response = requests.post(ENDPOINT, request_body, header)
    print(response.json())
    print("Request Header", response.request.headers)
    print("Response Header", response.headers)
    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"