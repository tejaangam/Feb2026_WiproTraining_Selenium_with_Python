import pytest
import requests


BASE_URL = "https://httpbin.org/status"


@pytest.mark.parametrize("status_code", [200, 400, 401, 500])
def test_multiple_status_codes(status_code):
    response = requests.get(f"{BASE_URL}/{status_code}")

    assert response.status_code == status_code