import requests
from jsonschema import validate

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_user_schema_validation():
    # Call API
    response = requests.get(f"{BASE_URL}/users/1")

    # Status check
    assert response.status_code == 200

    # JSON response
    data = response.json()

    # Expected JSON schema
    user_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "name": {"type": "string"},
            "username": {"type": "string"},
            "email": {"type": "string"},
            "address": {
                "type": "object",
                "properties": {
                    "street": {"type": "string"},
                    "city": {"type": "string"}
                },
                "required": ["street", "city"]
            },
            "phone": {"type": "string"},
            "website": {"type": "string"}
        },
        "required": ["id", "name", "email"]
    }

    # Validate schema
    validate(instance=data, schema=user_schema)
