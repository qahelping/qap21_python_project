from datetime import datetime

import pytest
from logger import logger

from test_api.tms_service import TmsService


@pytest.fixture
def tms_service():
    return TmsService()


@pytest.fixture
def token(tms_service):
    # Очищаем pytest.token перед логином
    pytest.token = None
    response_json = tms_service.login("user1@example.com", "user1123")
    assert response_json["access_token"]
    pytest.token = response_json["access_token"]
    return pytest.token


def test_create_second_admin(tms_service):
    # Очищаем pytest.token перед регистрацией админа
    pytest.token = None
    response_json = tms_service.register_admin("admin2", "admin2@example.com", "qwerty123!", code=403)

    assert response_json["detail"] == "Admin already exists. Registration is disabled."
    logger.info(response_json)


def test_create_board(token, tms_service):
    response_json = tms_service.create_board("string", "string", False)

    logger.info(response_json)
    assert response_json["id"]
    assert response_json["archived"] is False
    assert response_json["created_by"]
    assert response_json["title"] == "string"
    assert response_json["description"] == "string"
    assert response_json["public"] is False

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)


def test_create_task(token, tms_service):
    # Сначала создаем доску
    board_response = tms_service.create_board("string", "string", False)
    logger.info(board_response)
    board_id = board_response["id"]

    # Создаем задачу
    response_json = tms_service.create_task(board_id, "Моя вторая задача", "Описание задачи", "todo", "high")

    assert response_json["id"]
    assert response_json["created_by"]
    assert response_json["title"] == "Моя вторая задача"
    assert response_json["status"] == "todo"
    assert response_json["priority"] == "high"

    current_date = datetime.now().strftime("%Y-%m-%d")
    assert response_json["created_at"].startswith(current_date)
    assert response_json["updated_at"].startswith(current_date)


def test_get_users(token, tms_service):
    response_json = tms_service.get_users(skip=0, limit=100)

    logger.info(response_json)
    assert response_json[0]["id"] == 1
    assert response_json[0]["username"] == "admin"
    assert response_json[0]["email"] == "user@example.com"
    assert response_json[0]["role"] == "admin"
    assert response_json[0]["avatar_url"] is None
    assert response_json[0]["created_at"] == "2025-11-24T18:12:15.321979"


def test_get_users_without_token(tms_service):
    # Очищаем pytest.token для теста без авторизации
    pytest.token = None
    response_json = tms_service.get_users(skip=0, limit=100, code=403)

    logger.info(response_json)
    assert response_json["detail"] == "Not authenticated"
