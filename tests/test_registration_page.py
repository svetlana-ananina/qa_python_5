import data
from urls import URLS as url
from locators import Locators as loc
import helpers
import pytest


@pytest.mark.usefixtures("get_driver")
class TestRegistrationPage:

    def test_registration_success(self, get_driver):
        ''' Проверка успешной регистрации '''
        # Открываем окно веб-драйвера
        driver = get_driver
        helpers.open_reg_window(driver)

        # Выполняем регистрацию нового пользователя
        helpers.register_new_user(driver)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Проверяем, что произошел переход на страницу авторизации
        helpers.wait_url_changes(driver, url.REG_PAGE_URL)
        assert driver.current_url == url.AUTH_PAGE_URL


    def test_registration_invalid_password_error_message(self, get_driver):
        ''' Проверка сообщения о некорректном пароле в форме регистрации '''
        # Открываем окно веб-драйвера и страницу регистрации
        driver = get_driver
        helpers.open_reg_window(driver)

        # Выполняем регистрацию нового пользователя
        helpers.register_new_user(driver, password=helpers.gen_invalid_password())

        # Ждем пока не появится сообщение об ошибке
        helpers.wait_element(driver, loc.REG_PAGE_ERROR_MESSAGE)
        elements = helpers.find_elements(driver, loc.REG_PAGE_ERROR_MESSAGE)

        # Проверяем, что появилось сообщение об ошибке и текст сообщения соответствует ошибке - неправильный пароль
        assert len(elements) == 1 and elements[0].text == data.DATA.INVALID_PASS_TEXT

