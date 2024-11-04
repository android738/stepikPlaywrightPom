import allure
import pytest


@allure.epic('Web Interface')
@allure.feature('Доступ к системе')
@allure.story('Аутентификация')
@allure.title('Некорректные данные')
@allure.description('Тест аутентификации в системе с некорректными данными пользователя')
@allure.severity(allure.severity_level.MINOR)
def test_login_failure(login_page):
    with allure.step("Открыть страницу аутентификации."):
        login_page.navigate()
    with allure.step("Попытаться пройти аутентификацию."):
        login_page.login('1', '2')
    assert login_page.get_error_message() == 'Invalid credentials. Please try again.'


@pytest.mark.parametrize('username, password', [
    ('user', 'user'),
    ('admin', 'admin')
])
def test_login_success(login_page, dashboard_page, username, password):
    login_page.navigate()
    login_page.login(username, password)
    dashboard_page.assert_welcome_message(f'Welcome {username}')
