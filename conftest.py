import time

import pytest
from faker import Faker

from config import SESSION, BASE_URL
from lib.utils import build_request_headers

fake = Faker()
create_user_url = "/api/v1/user/"
login_url = "/api/v1/auth/login"

@pytest.fixture(scope="module")
def create_user_payload():
    username = f"user_{int(time.time())}"
    return {
        "username": username,
        "password": "test123",
        "role": "user",
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "state": "Lagos"
    }

@pytest.fixture(scope="module")
def created_user(create_user_payload):
    headers = build_request_headers(content_type="application/json")
    response = SESSION.post(f"{BASE_URL}{create_user_url}", headers=headers, json=create_user_payload)
    return {**create_user_payload, **response.json()}


@pytest.fixture(scope="module")
def login_payload(create_user_payload):
    return {
        "username": create_user_payload["username"],
        "password": create_user_payload["password"],
        "role": create_user_payload["role"]
    }

@pytest.fixture(scope="module")
def user_access_token(login_payload):
    headers = build_request_headers(content_type="application/json")
    response = SESSION.post(f"{BASE_URL}{login_url}", headers=headers, json=login_payload)
    token = response.json().get("accessToken")
    return token

