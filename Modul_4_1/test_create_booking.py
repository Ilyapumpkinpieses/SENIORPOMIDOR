import requests
import pytest
from requests import session


class TestBookings:
    BASE_URL="https://restful-booker.herokuapp.com"
    HEADERS={"Content-Type": "application/json","Accept":"application/json"}
    json={"username" : "admin","password" : "password123"}
    def get_token(self):
        response= requests.post(f"{self.BASE_URL}/auth", headers=self.HEADERS,json=self.json)
        assert response.status_code == 200, "ошибка авторизации"
        token = response.json().get("token")
        assert token is not None, "В ответе не оказалось токена"
        return token
    def test_create_booking(self):
        session = requests.Session()
        session.headers.update(self.HEADERS)

        token = self.get_token()
        session.headers.update({"Cookie": f"token={token}"})

        booking_data={"firstname" : "John",
    "lastname" : "Smith",
    "totalprice" : 111,
    "depositpaid" : True,
    "bookingdates" : {
        "checkin" : "2018-01-01",
        "checkout" : "2019-01-01"
    },
    "additionalneeds" : "Breakfast"}

        create_booking = session.post(f"{self.BASE_URL}/booking", json=booking_data)
        assert create_booking.status_code == 200, "ошибка при создании брони"
        booking_id = create_booking.json().get("bookingid")
        assert booking_id is not None, "индефикатор брони не найден"
        assert create_booking.json()["booking"]["firstname"]=="John", "заданное имя не совпадает"
        assert create_booking.json()["booking"]["totalprice"] == 111, "заданная стоимость не совпадает"

        get_booking = session.get(f"{self.BASE_URL}//booking/:{booking_id}")
        assert get_booking.status_code == 200, "бронь не найдена"
        assert get_booking.json()["lastname"] == "Smith", "заданная фамилия не совпадает"

        deleted_booking = session.delete(f"{self.BASE_URL}/booking/{booking_id}")
        assert deleted_booking.status_code == 201, ",Бронь не найдена"

        get_booking = session.get(f"{self.BASE_URL}//booking/:{booking_id}")
        assert get_booking.status_code == 404, "<Бронь не удалилась>"
