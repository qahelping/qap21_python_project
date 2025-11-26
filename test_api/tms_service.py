from test_api.base_sevice import BaseService

DOMAIN = "http://localhost:8000"


class TmsService(BaseService):

    def login(self, email, password):
        """
        Авторизация пользователя
        :param email: email пользователя
        :param password: пароль пользователя
        :return: словарь с access_token
        """
        url = f"{DOMAIN}/auth/login"
        body = {"email": email, "password": password}
        # Для login не нужен токен, поэтому передаем None
        response = self.post(url, token=None, body=body, code=200)
        return response

    def register_admin(self, username, email, password, code=None):
        """
        Регистрация администратора
        :param username: имя пользователя
        :param email: email пользователя
        :param password: пароль пользователя
        :param code: ожидаемый HTTP статус код (опционально)
        :return: ответ от сервера
        """
        url = f"{DOMAIN}/auth/register-admin"
        body = {"username": username, "email": email, "password": password}
        # Для register-admin не нужен токен
        response = self.post(url, token=None, body=body, code=code)
        return response

    def create_board(self, title, description, public):
        """
        Создание доски
        :param title: название доски
        :param description: описание доски
        :param public: публичная ли доска (bool)
        :return: ответ от сервера с данными созданной доски
        """
        url = f"{DOMAIN}/boards/"
        body = {"title": title, "description": description, "public": public}
        # Токен берется из pytest.token автоматически
        response = self.post(url, token=None, body=body, code=201)
        return response

    def create_task(self, board_id, title, description, status, priority):
        """
        Создание задачи в доске
        :param board_id: ID доски
        :param title: название задачи
        :param description: описание задачи
        :param status: статус задачи
        :param priority: приоритет задачи
        :return: ответ от сервера с данными созданной задачи
        """
        url = f"{DOMAIN}/boards/{board_id}/tasks"
        body = {"title": title, "description": description, "status": status, "priority": priority}
        # Токен берется из pytest.token автоматически
        response = self.post(url, token=None, body=body, code=201)
        return response

    def get_users(self, skip=0, limit=100, code=200):
        """
        Получение списка пользователей
        :param skip: количество пропущенных записей
        :param limit: максимальное количество записей
        :param code: ожидаемый HTTP статус код (по умолчанию 200)
        :return: список пользователей
        """
        url = f"{DOMAIN}/users/?skip={skip}&limit={limit}"
        # Токен берется из pytest.token автоматически
        response = self.get(url, code=code)
        return response
