import data
from urls import URLS as url
from locators import Locators as loc
import helpers


class TestRegistrationPage:

    def test_registration_success(self, open_reg_window,
                                  gen_login, gen_password, get_user_name):
        ''' Проверка успешной регистрации '''
        driver = open_reg_window  # Функция-фикстура открывает окно веб-драйвера и страницу регистрации

        name = get_user_name                                        # Получаем данные для регистрации
        login = gen_login                                           # Генерирует логин по шаблону
        password = gen_password                                     # Генерирует пароль

        helpers.wait_element(driver, loc.REG_BUTTON)                # Ждем появления кнопки 'Зарегистрироваться'

        helpers.set_value(driver, loc.USER_NAME_INPUT, name)        # Вводим данные в поля и кликаем кнопку
        helpers.set_value(driver, loc.USER_EMAIL_INPUT, login)
        helpers.set_value(driver, loc.USER_PASSWORD_INPUT, password)

        helpers.click_element(driver, loc.REG_BUTTON)

        helpers.wait_url_changes(driver, url.REG_PAGE_URL)          # Проверяем, что произошел переход на страницу авторизации
        assert driver.current_url == url.AUTH_PAGE_URL

        driver.quit()

    def test_registration_invalid_password_error_message(self, open_reg_window,
                                                         gen_login, get_user_name, gen_invalid_password):
        ''' Проверка сообщения о некорректном пароле в форме регистрации '''

        driver = open_reg_window                                    # Открываем страницу регистрации и ждем появления формы регистрации

        name = get_user_name                                        # Получаем данные для регистрации
        login = gen_login                                           # Генерирует логин по шаблону
        password = gen_invalid_password                             # Генерирует пароль

        helpers.wait_element(driver, loc.REG_BUTTON)                # Ждем появления кнопки 'Зарегистрироваться'

        helpers.set_value(driver, loc.USER_NAME_INPUT, name)        # Вводим данные в поля и кликаем кнопку
        helpers.set_value(driver, loc.USER_EMAIL_INPUT, login)
        helpers.set_value(driver, loc.USER_PASSWORD_INPUT, password)

        helpers.click_element(driver, loc.REG_BUTTON)

        helpers.wait_element(driver, loc.REG_PAGE_ERROR_MESSAGE)    # Ждем пока не появится сообщение об ошибке
        elements = helpers.find_elements(driver, loc.REG_PAGE_ERROR_MESSAGE)
        assert len(elements) == 1 and elements[0].text == data.DATA.INVALID_PASS_TEXT

        driver.quit()
