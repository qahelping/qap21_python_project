import pytest
import requests
from logger import logger


class BaseService:

    @staticmethod
    def request(method, url, body, code):
        if pytest.token:
            headers = {"Authorization": f"Bearer {pytest.token}"}
        else:
            headers = None
        try:
            response = requests.request(method, url, headers=headers, json=body)
            if code is None:
                response.raise_for_status()
            else:
                assert response.status_code == code
            logger.info("OK. URL: %s, Code: %d", url, response.status_code)
            return response.json()
        except requests.exceptions.RequestException as e:
            logger.error("Error. %s", str(e))
            return None

    def delete(self, url, body=None, code=None):
        self.request("DELETE", url, body, code)

    def post(self, url, token, body=None, code=None):
        self.request("POST", url, body, code)

    def put(self, url, body=None, code=None):
        self.request("POST", url, body, code)

    def get(self, url, code=None):
        self.request("POST", url, None, code)
