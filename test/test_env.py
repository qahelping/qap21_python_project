import os

import pytest


@pytest.mark.env
def test_env_data():
    print(os.getenv("API_URL"))
    print(os.getenv("TOKEN"))
    print(os.getenv("LOGIN"))
