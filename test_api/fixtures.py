import pytest


@pytest.fixture
def common():
    """Fixture for save and transactions test values between steps, for example data class for module."""

    class Common:
        def __getattr__(self, item):
            return self.__dict__.get(item)

    return Common()
