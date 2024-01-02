import requests

ENDPOINT = 'https://reqres.in/api/users/2'


def test_delete_user():

    response = requests.delete(ENDPOINT)
    assert response.status_code == 204
