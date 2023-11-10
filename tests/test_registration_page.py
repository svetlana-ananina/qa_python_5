import data
from urls import URLS as url
from locators import Locators as loc
import helpers


class TestRegistrationPage:

    def test_registration_success(self, open_reg_window,
                                  gen_login, gen_password, get_user_name):
        ''' Проверка успешной регистрации '''
        driver = open_reg_window  # Функция-фикстура открывает окно веб-драйвера и страницу регистрации

        # Получаем данные для регистрации
        name = get_user_name
        login = gen_login  # Генерирует логин по шаблону
        password = gen_password  # Генерирует пароль

        # Ждем появления кнопки 'Зарегистрироваться'
        helpers.wait_element(driver, loc.REG_BUTTON)

        # Вводим данные в поля и кликаем кнопку
        helpers.set_value(driver, loc.USER_NAME_INPUT, name)
        helpers.set_value(driver, loc.USER_EMAIL_INPUT, login)
        helpers.set_value(driver, loc.USER_PASSWORD_INPUT, password)

        helpers.click_element(driver, loc.REG_BUTTON)

        # Проверяем, что произошел переход на страницу авторизации
        helpers.wait_url_changes(driver, url.REG_PAGE_URL)
        assert driver.current_url == url.AUTH_PAGE_URL

        driver.quit()

    def test_registration_invalid_password_error_message(self, open_reg_window,
                                                         gen_login, get_user_name, gen_invalid_password):
        ''' Проверка сообщения о некорректном пароле в форме регистрации '''

        # Открываем страницу регистрации по прямой ссылке и ждем появления формы регистрации
        driver = open_reg_window  # Функция-фикстура открывает окно веб-драйвера и страницу регистрации

        # Получаем данные для регистрации
        name = get_user_name
        login = gen_login  # Генерирует логин по шаблону
        password = gen_invalid_password  # Генерирует пароль

        # Ждем появления кнопки 'Зарегистрироваться'
        helpers.wait_element(driver, loc.REG_BUTTON)

        # Вводим данные в поля и кликаем кнопку
        helpers.set_value(driver, loc.USER_NAME_INPUT, name)
        helpers.set_value(driver, loc.USER_EMAIL_INPUT, login)
        helpers.set_value(driver, loc.USER_PASSWORD_INPUT, password)

        helpers.click_element(driver, loc.REG_BUTTON)

        # Ждем пока не появится сообщение об ошибке
        helpers.wait_element(driver, loc.REG_PAGE_ERROR_MESSAGE)
        elements = helpers.find_elements(driver, loc.REG_PAGE_ERROR_MESSAGE)
        assert len(elements) == 1 and elements[0].text == data.DATA.INVALID_PASS_TEXT

        driver.quit()
