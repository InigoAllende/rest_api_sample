import pytest

from src.api.main import app
from src.api.db.db_logic import _create_connection

def _clean_db():
    with _create_connection() as conn:
        conn.execute(f'DELETE FROM users;')


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
    _clean_db()