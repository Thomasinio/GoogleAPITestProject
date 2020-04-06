import pytest

from src.api.helpers.auth_helper import get_authorization


def pytest_addoption(parser):
    parser.addoption("--access_token", action="store", default="default name")


@pytest.fixture(scope="session")
def calendar_fixture(request):
    if request.config.option.access_token:
        return "Bearer " + request.config.option.access_token
    return get_authorization()
