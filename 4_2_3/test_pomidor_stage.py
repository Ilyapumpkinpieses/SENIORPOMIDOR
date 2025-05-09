import pytest
from constantes import BASE_URL


class TestItems:
    endpoint = f"{BASE_URL}/items/"

    def test_create_item(self, item_data, new_item_data, auth_session):
        response = auth_session.post(self.endpoint, json=item_data)
        assert response.status_code in (
            200,
            201,
        ), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        item_id = data.get("id")
        assert item_id is not None, "Item ID не должен быть None"
        assert isinstance(item_id, int), "Item ID должен быть целым числом"
        assert data.get("title") == item_data["title"], "Название не соответствует"
        assert data.get("description") == item_data["description"], "Описание не соответствует"

        assert "created_at" in data, "Отсутствует дата создания"
        assert "updated_at" in data, "Отсутствует дата обновления"

        self.created_item_id = item_id

        change_item = auth_session.put(f"{self.endpoint}{item_id}", json=new_item_data)
        assert (
                change_item.status_code == 200
        ), f"Response: {response.status_code}, {response.text}"

        updated_data = change_item.json()
        assert updated_data["title"] == new_item_data["title"], "Название не обновилось"
        assert updated_data["description"] == new_item_data["description"], "Описание не обновилось"
        assert updated_data["updated_at"] != data["updated_at"], "Дата обновления не изменилась"

        get_item = auth_session.get(f"{self.endpoint}{item_id}")
        assert get_item.status_code == 200, "Не удалось получить элемент"
        get_data = get_item.json()
        assert get_data["id"] == item_id, "ID полученного элемента не совпадает"

        delete_item = auth_session.delete(f"{self.endpoint}{item_id}")
        assert (
                delete_item.status_code == 200
        ), f"Response: {response.status_code}, {response.text}"


        check_deleted = auth_session.get(f"{self.endpoint}{item_id}")
        assert check_deleted.status_code == 404, "Элемент не был удален"

    def test_get_items(self, auth_session):
        response = auth_session.get(self.endpoint)
        assert (
                response.status_code == 200
        ), f"Response: {response.status_code}, {response.text}"

        data = response.json()
        assert "data" in data, "Response missing 'data' key"
        assert isinstance(data["data"], list), "'data' is not a list"
        assert isinstance(data.get("count"), int), "'count' should be integer"

        assert "total" in data, "Отсутствует общее количество элементов"
        assert "pagea" in data, "Отсутствует номер страницы"
        assert "size" in data, "Отсутствует размер страницы"

        if len(data["data"]) > 0:
            item = data["data"][0]
            assert "id" in item, "Элемент не содержит ID"
            assert "title" in item, "Элемент не содержит title"
            assert "description" in item, "Элемент не содержит description"

    def test_create_item_validation(self, auth_session, invalid_item_data):
        response = auth_session.post(self.endpoint, json=invalid_item_data)
        assert response.status_code == 422, "Ожидалась ошибка валидации"

        error_data = response.json()
        assert "detail" in error_data, "Отсутствует описание ошибки"
        assert isinstance(error_data["detail"], list), "Ошибки должны быть в виде списка"

    def test_get_nonexistent_item(self, auth_session):
        response = auth_session.get(f"{self.endpoint}999999")
        assert response.status_code == 404, "Ожидалась ошибка 404 для несуществующего элемента"