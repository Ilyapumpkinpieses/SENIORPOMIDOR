import requests
import pytest

from conftest import auth_session
from constant import BASE_URL

class TestBooking:
    endpoint = f"{BASE_URL}/booking"
    booking_id = None
    def test_create_booking(self,booking_data,auth_session):
        create_booking = auth_session.post(self.endpoint,json=booking_data["create"])
        assert create_booking.status_code == 200,"Бронирование не создано"
        create_response = create_booking.json()
        self.__class__.booking_id = create_booking.json().get("bookingid")
        assert self.__class__.booking_id is not None,"ID букинга не найден в ответе"
        booking_details = create_response.get("booking", {})
        assert booking_details, "Данные о бронирования отсутствуют"
        assert booking_details is not None, "Данные бронирования не найдены"
        assert booking_details["firstname"] == booking_data["create"]["firstname"], "Имя не соответсвует заданному"
        assert booking_details["lastname"] == booking_data["create"]["lastname"], "Фамилия не соответсвует заданному"
        assert booking_details["totalprice"] == booking_data["create"]["totalprice"], "Цена не соответсвует заданному"
        assert booking_details["depositpaid"] == booking_data["create"]["depositpaid"], "Депозит не выдаётся"
        assert booking_details["bookingdates"] == booking_data["create"]["bookingdates"], "Даты заезда и выезда не совпадают"
        assert booking_details["additionalneeds"] == booking_data["create"]["additionalneeds"], "Предпочтение не совпадают"

    def test_get_all_booking(self, auth_session,booking_data):
        get_booking = auth_session.get(self.endpoint)
        assert get_booking.status_code == 200, f"Ошибка при получении созданных бронирований. Status code: {get_booking.status_code}"

    def test_path_booking(self,auth_session,booking_data):
        if not self.__class__.booking_id:
            pytest.skip("Необходимо сначала создать бронирование")
        url = f"{self.endpoint}/{self.__class__.booking_id}"
        patch_booking = auth_session.patch(url,json=booking_data["patch"])
        assert patch_booking.status_code == 200,"Бронирование частично не обновлено"
        get_patched = auth_session.get(url)
        patch_response = get_patched.json()
        assert patch_response is not None, "Обновленные данные не найдены"
        assert patch_response["firstname"] == booking_data["patch"]["firstname"], "Имя не совпадает"
        assert patch_response["lastname"] == booking_data["patch"]["lastname"], "Фамилия не совпадает"
        assert patch_response["additionalneeds"] == booking_data["patch"]["additionalneeds"], "Предпочтение не обновлены "

    def test_put_booking(self,auth_session,booking_data):
        if not self.__class__.booking_id:
            pytest.skip("Необходимо сначала создать бронирование")
        url = f"{self.endpoint}/{self.__class__.booking_id}"
        put_booking = auth_session.put(url, json = booking_data["put"])
        assert put_booking.status_code == 200, "Бронирование не обновлено полностью"
        get_put = auth_session.get(url)
        put_response = get_put.json()
        assert put_response is not None, "Данные бронирования не найдены в ответе"
        assert put_response["firstname"] == booking_data["put"]["firstname"], "Имя не обновлено "
        assert put_response["lastname"] == booking_data["put"]["lastname"], "Фамилия не обновлено "
        assert put_response["totalprice"] == booking_data["put"]["totalprice"], "Полная сумма не обновлена "
        assert put_response["depositpaid"] == booking_data["put"]["depositpaid"], "Депозит не обновлен"
        assert put_response["bookingdates"] == booking_data["put"]["bookingdates"], "Даты заезда и выезда не обновлены "
        assert put_response["additionalneeds"] == booking_data["put"]["additionalneeds"], "Предпочтение не обновлено "

    def test_delete_booking(self,auth_session):
        if not self.__class__.booking_id:
            pytest.skip("Необходимо сначала создать бронирование")
        url = f"{self.endpoint}/{self.__class__.booking_id}"
        delete_booking = auth_session.delete(url)
        assert delete_booking.status_code == 201, f"Ошибка  удаления букинга с ID {self.__class__.booking_id}"

    def test_check_delete_booking(self, auth_session):
        if not self.__class__.booking_id:
            pytest.skip("Необходимо сначала создать бронирование")
        url = f"{self.endpoint}/{self.__class__.booking_id}"
        check_delete_booking = auth_session.get(url)
        assert check_delete_booking.status_code == 404, f"Букинг с ID {self.__class__.booking_id} не удален"