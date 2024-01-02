import requests

ENDPOINT = 'https://reqres.in/api/users/2'


def test_partiallyupdate_user():
    request_body = {
        "Job": "CFO"
    }

    response = requests.patch(ENDPOINT, request_body)
    print(response.text)
    assert response.status_code == 200
    response_body = response.json()
    assert response_body["Job"] == "CFO"