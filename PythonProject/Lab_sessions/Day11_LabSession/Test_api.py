import requests

def test_get_profile(base_url, auth_token):
    headers = {"Authorization": f"Bearer {auth_token}"}

    response = requests.get(f"{base_url}/users/1", headers=headers)

    assert response.status_code == 200
