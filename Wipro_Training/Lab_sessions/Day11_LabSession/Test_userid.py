import requests


def test_get_user(test_user):
    user_id = test_user["id"]

    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")

    assert response.status_code == 200
