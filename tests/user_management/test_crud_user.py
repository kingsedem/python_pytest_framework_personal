import time

import pytest
from faker import Faker
from config import SESSION, BASE_URL
from lib.utils import build_request_headers

fake = Faker()

create_user_url = "/api/v1/user/"
login_url = "/api/v1/auth/login"

@pytest.mark.regression_test
def test_send_post_create_user_is_201_and_id_is_integer():
    username = f"user_{int(time.time())}"
    create_user_payload = { "username": username,
                            "password": "test123",
                            "role": "user",
                            "firstName": fake.first_name(),
                             "lastName": fake.last_name(),
                             "state": "Lagos" }
    headers = build_request_headers(content_type="application/json")
    response = SESSION.post(f"{BASE_URL}{create_user_url}", headers=headers, json=create_user_payload)

    print(response.json())
    created_userId = response.json()["userId"]
    assert response.status_code == 201
    assert created_userId is not None
    assert response.json().get("message") == "User created successfully"

@pytest.mark.sanity_test
def test_login_user_is_201_and_returns_access_token(created_user):
    headers = build_request_headers(content_type="application/json")
    login_payload = {
        "username": created_user["username"],
        "password": created_user["password"],
        "role": created_user["role"]
    }
    response = SESSION.post(f"{BASE_URL}{login_url}", headers=headers, json=login_payload)
    print(response.json())
    access_token = response.json()["accessToken"]
    print(access_token)
    assert response.status_code == 201
    assert "accessToken" in response.json()


@pytest.mark.smoke_test
def test_get_user_by_id_is_200_and_returns_created_firstname(created_user, user_access_token):
    headers = build_request_headers(content_type="application/json", access_token=user_access_token)
    response = SESSION.get(f"{BASE_URL}/api/v1/user/{created_user["userId"]}",
                           headers=headers)

    print(response.json())
    created_firstname = response.json().get("firstName")
    assert response.status_code == 200
    assert created_firstname is not None

@pytest.mark.regression_test
def test_full_update_user_by_id_is_200_and_returns_correct_message(created_user, user_access_token):
    headers = build_request_headers(content_type="application/json", access_token=user_access_token)
    full_update_payload = {
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
         "state": "Abuja"
    }
    response = SESSION.put(f"{BASE_URL}/api/v1/user/{created_user["userId"]}",
                           headers=headers, json=full_update_payload)
    print(response.json())
    assert response.status_code == 200
    assert response.json().get("message") == "User updated successfully"

@pytest.mark.sanity_test
def test_full_update_user_by_id_changes_firstname(created_user, user_access_token):
    headers = build_request_headers(content_type="application/json", access_token=user_access_token)
    response = SESSION.get(f"{BASE_URL}/api/v1/user/{created_user["userId"]}",
                           headers=headers)
    print(response.json())
    updated_firstname = response.json().get("firstName")
    assert updated_firstname is not None
    assert updated_firstname != created_user["firstName"]

@pytest.mark.smoke_test
def test_patch_user_by_id_returns_200(created_user, user_access_token):
    headers = build_request_headers(content_type="application/json", access_token=user_access_token)
    partial_update_payload = {
        "lastName": fake.last_name()
    }
    response = SESSION.patch(f"{BASE_URL}/api/v1/user/{created_user["userId"]}",
                           headers=headers, json=partial_update_payload)
    print(response.json())
    updated_lastname = response.json().get("firstName")
    assert response.status_code == 200
    assert response.json().get("message") == "User updated successfully"

@pytest.mark.sanity_test
def test_partial_update_user_by_id_changes_lastname(created_user, user_access_token):
    headers = build_request_headers(content_type="application/json", access_token=user_access_token)
    response = SESSION.get(f"{BASE_URL}/api/v1/user/{created_user["userId"]}",
                           headers=headers)
    print(response.json())
    updated_lastname = response.json().get("lastName")
    assert updated_lastname is not None
    assert updated_lastname != created_user["lastName"]

@pytest.mark.regression_test
def test_delete_user(created_user, user_access_token):
    headers = build_request_headers(content_type="application/json", access_token=user_access_token)
    response = SESSION.delete(f"{BASE_URL}/api/v1/user/{created_user["userId"]}",
                           headers=headers)
    assert response.status_code == 200
    assert response.json().get("message") == "User deleted successfully"
