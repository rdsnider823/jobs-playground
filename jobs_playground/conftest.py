import dotenv
import pytest

from jobs_playground.users.models import User
from jobs_playground.users.tests.factories import UserFactory

# def pytest_sessionstart(session):
#     dotenv.load_dotenv("./.envs/.local/.django")
#     dotenv.load_dotenv("./.envs/.local/.redis")


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def user(db) -> User:
    return UserFactory()
