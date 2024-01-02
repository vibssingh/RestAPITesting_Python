import requests

ENDPOINT = 'https://reqres.in/api/users/2'


def test_update_user():
    request_body = {
        "name": "Vibha",
        "Job": "CTO"
    }

    response = requests.put(ENDPOINT, request_body)
    print(response.text)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["Job"] == "CTO"