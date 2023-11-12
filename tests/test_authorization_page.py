from urls import URLS as url
from locators import Locators as loc
import helpers


class TestAuthorization:

    def test_auth_from_main_page_login_button(self, register_new_user):
        """ Проверка регистрации с главной страницы через кнопку "Войти в аккаунт" """
        driver, reg_data = register_new_user                        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        driver.get(url.MAIN_PAGE_URL)                               # Открываем главную страницу

        helpers.wait_url(driver, url.MAIN_PAGE_URL)                 # Ждем, когда откроется главная страница и
        helpers.wait_element(driver, loc.MAIN_PAGE_LOGIN_BUTTON)    # появится кнопка "Войти в аккаунт"/"Оформить заказ"

        helpers.click_element(driver, loc.MAIN_PAGE_LOGIN_BUTTON)

        # Выполняем авторизацию
        assert helpers.sign_in(driver, login, password)


    def test_auth_from_main_page_profile_button(self, register_new_user):
        ''' Проверка входа с главной страницы через кнопку "Личный Кабинет" '''
        driver, reg_data = register_new_user                        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        driver.get(url.MAIN_PAGE_URL)                               # Открываем главную страницу

        helpers.wait_url(driver, url.MAIN_PAGE_URL)                 # Ждем, когда откроется главная страница и появится ссылка "Личный кабинет"
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        assert helpers.sign_in(driver, login, password)             # Выполняем авторизацию


    def test_auth_from_reg_page(self, register_new_user):
        ''' Проверка входа через ссылку "Войти" на странице регистрации '''
        driver, reg_data = register_new_user                        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        driver.get(url.REG_PAGE_URL)                                # Открываем страницу регистрации и ждем появления ссылки "Войти"

        helpers.wait_url(driver, url.REG_PAGE_URL)
        helpers.wait_element(driver, loc.REG_PAGE_LOGIN_LINK)

        helpers.click_element(driver, loc.REG_PAGE_LOGIN_LINK)      # Кликаем по ссылке "Войти" и переходим на страницу авторизации

        assert helpers.sign_in(driver, login, password)             # Выполняем авторизацию


    def test_auth_from_pass_recover_page(self, register_new_user):
        ''' Проверка входа через ссылку "Войти" на странице восстановления пароля '''
        driver, reg_data = register_new_user                        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        driver.get(url.RECOVER_PAGE_URL)                            # Открываем страницу восстановления пароля и ждем появления ссылки "Войти"

        helpers.wait_url(driver, url.RECOVER_PAGE_URL)
        helpers.wait_element(driver, loc.RECOVER_PAGE_LINK)

        helpers.click_element(driver, loc.RECOVER_PAGE_LINK)        # Кликаем по ссылке "Войти" и переходим на страницу авторизации

        # Выполняем авторизацию
        assert helpers.sign_in(driver, login, password)

