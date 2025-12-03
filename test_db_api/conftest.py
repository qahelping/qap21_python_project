import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from test_db_api.config import settings


@pytest.fixture
def db_session():
    # Создание движка базы данных
    engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})  # Необходимо для SQLite

    # Создание сессии
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal()
