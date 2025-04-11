import pytest
import requests
from faker import Faker
fake = Faker()

from constant import HEADERS, BASE_URL
from datetime import datetime, timedelta

@pytest.fixture(scope = "session")
def auth_session():
    session = requests.session()
    session.headers.update(HEADERS)

    auth_response = session.post(f"{BASE_URL}/auth", json={"username": "admin", "password": "password123"})
    assert auth_response.status_code == 200 , "Ошибка авторторизации"
    token = auth_response.json().get("token")
    assert token is not None, "Токен не найден в ответе"
    session.headers.update({"Cookie": f"token={token}"})
    return session

@pytest.fixture()
def booking_data():
    create_data = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "totalprice": fake.random_int(min=100, max=3000),
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-04-05",
            "checkout": "2024-04-08"
        },
        "additionalneeds": fake.random_element(elements = ("Breakfast", "Dinner", "WiFi", "Parking","swimming pool"))
        }
    patch_data = {
        "firstname": fake.first_name(),
        "lastname": fake.last_name(),
        "additionalneeds": fake.random_element(elements = ("Breakfast", "Dinner", "WiFi", "Parking","swimming pool"))
        }
    put_data = {
        "firstname": "FULL_UPDATE_" + fake.first_name(),
        "lastname": "FULL_UPDATE_" + fake.last_name(),
        "totalprice": fake.random_int(min=100, max=3000),
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2024-04-15",
            "checkout": "2024-04-28"
        },
        "additionalneeds": "FULL_UPDATE_" + fake.random_element(elements = ("Breakfast", "Dinner", "WiFi", "Parking","swimming pool"))
        }
    return {
        "create" : create_data,
        "patch" : patch_data,
        "put" : put_data
        }