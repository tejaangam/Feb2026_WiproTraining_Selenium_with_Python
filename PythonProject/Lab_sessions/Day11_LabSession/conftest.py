#1.Write a pytest fixture that generates an authentication token once per session and use it in multiple API test cases.

#confest file
import pytest
import requests


@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"


@pytest.fixture(scope="session")
def auth_token():
    # dummy token (this API does not need login)
    return "dummy_token"


BASE_URL = "https://jsonplaceholder.typicode.com"
@pytest.fixture
def test_user():
    # ---------- Setup (Create User) ----------
    payload = {
        "name": "Test User",
        "email": "testuser@example.com"
    }

    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code in [200, 201]

    user_data = response.json()
    user_id = user_data.get("id")

    print(f"\nCreated user with ID: {user_id}")

    # Give control to test
    yield user_data

    # ---------- Teardown (Delete User) ----------
    delete_response = requests.delete(f"{BASE_URL}/users/{user_id}")

    print(f"\nDeleted user with ID: {user_id}")
    assert delete_response.status_code in [200, 204]

#FIxture Chain

# ---------- Level 1 ----------
@pytest.fixture
def base_url():
    url = "https://jsonplaceholder.typicode.com"
    print("\n[base_url] setup")
    return url


# ---------- Level 2 ----------
@pytest.fixture
def auth_token(base_url):
    print("[auth_token] setup using base_url")

    # Example token (mocked for demo)
    token = "dummy_token_123"

    headers = {
        "Authorization": f"Bearer {token}"
    }
    return headers


# ---------- Level 3 ----------
@pytest.fixture
def user(base_url, auth_token):
    print("[user] setup using base_url + auth_token")

    payload = {
        "name": "Test User",
        "email": "test@example.com"
    }

    response = requests.post(f"{base_url}/users",
                             json=payload,
                             headers=auth_token)

    user_data = response.json()

    yield user_data

    print("[user] teardown (delete user)")
    requests.delete(f"{base_url}/users/{user_data.get('id')}")