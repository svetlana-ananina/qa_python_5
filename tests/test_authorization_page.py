from urls import URLS as url
from locators import Locators as loc
import helpers


class TestAuthorization:

    def test_auth_from_main_page_login_button(self, register_new_user):
        """ Проверка регистрации с главной страницы через кнопку "Войти в аккаунт" """
        # Выполняем регистрацию и открываем окно браузера перед запуском теста
        #    в функции-фикстуре register_new_user()
        driver, reg_data = register_new_user        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        # Открываем главную страницу
        driver.get(url.MAIN_PAGE_URL)

        # Ждем, когда откроется главная страница и появится кнопка "Войти в аккаунт"/"Оформить заказ"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_LOGIN_BUTTON)

        helpers.click_element(driver, loc.MAIN_PAGE_LOGIN_BUTTON)

        # Выполняем авторизацию
        assert helpers.sign_in(driver, login, password)


    def test_auth_from_main_page_profile_button(self, register_new_user):
        ''' Проверка входа с главной страницы через кнопку "Личный Кабинет" '''
        # Выполняем регистрацию и открываем окно браузера перед запуском теста
        #    в функции-фикстуре класса register_new_user
        driver, reg_data = register_new_user        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        # Открываем главную страницу
        driver.get(url.MAIN_PAGE_URL)

        # Ждем, когда откроется главная страница и появится ссылка "Личный кабинет"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Выполняем авторизацию
        assert helpers.sign_in(driver, login, password)


    def test_auth_from_reg_page(self, register_new_user):
        ''' Проверка входа через ссылку "Войти" на странице регистрации '''
        # Выполняем регистрацию и открываем окно браузера перед запуском теста
        #    в функции-фикстуре класса register_new_user
        driver, reg_data = register_new_user        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        # Открываем страницу регистрации и ждем появления ссылки "Войти"
        driver.get(url.REG_PAGE_URL)

        helpers.wait_url(driver, url.REG_PAGE_URL)
        helpers.wait_element(driver, loc.REG_PAGE_LOGIN_LINK)

        # Кликаем по ссылке "Войти" и переходим на страницу авторизации
        helpers.click_element(driver, loc.REG_PAGE_LOGIN_LINK)

        # Выполняем авторизацию
        assert helpers.sign_in(driver, login, password)


    def test_auth_from_pass_recover_page(self, register_new_user):
        ''' Проверка входа через ссылку "Войти" на странице восстановления пароля '''
        # Выполняем регистрацию и открываем окно браузера перед запуском теста
        #    в функции-фикстуре класса register_new_user
        driver, reg_data = register_new_user        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        # Открываем страницу восстановления пароля и ждем появления ссылки "Войти"
        driver.get(url.RECOVER_PAGE_URL)

        helpers.wait_url(driver, url.RECOVER_PAGE_URL)
        helpers.wait_element(driver, loc.RECOVER_PAGE_LINK)

        # Кликаем по ссылке "Войти" и переходим на страницу авторизации
        helpers.click_element(driver, loc.RECOVER_PAGE_LINK)

        # Выполняем авторизацию
        assert helpers.sign_in(driver, login, password)

