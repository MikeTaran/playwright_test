import pytest
from pages.main_page import Main


@pytest.fixture(scope='class')
def user_login(browser, request):
    role_marker = request.node.get_closest_marker("role")  # Получаем значение маркера
    role = role_marker.args[0] if role_marker else None  # Извлекаем значение роли
    m = Main(browser)
    m.user_login(role)
