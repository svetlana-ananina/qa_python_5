from urls import URLS as url
from locators import Locators as loc
import helpers
from selenium import webdriver
import pytest


@pytest.mark.usefixtures("get_driver")
class TestAuthorization:

    def test_auth_from_main_page_login_button(self, get_driver):
        """ Проверка регистрации с главной страницы через кнопку "Войти в аккаунт" """
        # Выполняем регистрацию и авторизацию нового пользователя
        # Открываем окно веб-драйвера и страницу регистрации
        driver = get_driver
        helpers.open_reg_window(driver)

        # Вызываем функцию регистрации, сохраняем логин и пароль
        login, password = helpers.register_new_user(driver)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Открываем главную страницу
        helpers.open_main_window(driver)

        # Ждем, когда откроется главная страница и появится кнопка "Войти в аккаунт"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_LOGIN_BUTTON)

        # Кликаем кнопку "Войти в аккаунт"
        helpers.click_element(driver, loc.MAIN_PAGE_LOGIN_BUTTON)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Вызываем функцию авторизации с сохраненными логином и паролем
        helpers.sign_in(driver, login, password)

        # Ждем Главную страницу и кнопку "Оформить заказ"/"Войти в аккаунт"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)

        # Проверяем, что на Главной странице появилась кнопка "Оформить заказ" вместо "Войти в аккаунт"
        assert helpers.check_order_button(driver)


    def test_auth_from_main_page_profile_button(self, get_driver):
        ''' Проверка входа с главной страницы через кнопку "Личный Кабинет" '''
        # Открываем окно веб-драйвера и страницу регистрации
        driver = get_driver
        helpers.open_reg_window(driver)

        # Выполняем регистрацию нового пользователя, сохраняем логин и пароль
        login, password = helpers.register_new_user(driver)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Открываем главную страницу
        helpers.open_main_window(driver)

        # Ждем, когда откроется главная страница и появится кнопка "Личный кабинет"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Кликаем кнопку "Личный кабинет"
        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Выполняем авторизацию
        helpers.sign_in(driver, login, password)

        # Ждем главную страницу и кнопку "Войти/оформить"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)

        # Проверяем, что на главной странице появилась кнопка "Оформить заказ"
        assert helpers.check_order_button(driver)


    def test_auth_from_reg_page(self, get_driver):
        ''' Проверка входа через ссылку "Войти" на странице регистрации '''
        # Открываем окно веб-драйвера и страницу регистрации
        driver = get_driver
        helpers.open_reg_window(driver)

        # Выполняем регистрацию нового пользователя, сохраняем логин и пароль
        login, password = helpers.register_new_user(driver)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Открываем страницу регистрации
        driver.get(url.REG_PAGE_URL)

        # Ждем страницу регистрации и текст с гиперссылкой "Войти"
        helpers.wait_url(driver, url.REG_PAGE_URL)
        helpers.wait_element(driver, loc.REG_PAGE_LOGIN_LINK)

        # Кликаем по ссылке "Войти"
        helpers.click_element(driver, loc.REG_PAGE_LOGIN_LINK)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Выполняем авторизацию
        helpers.sign_in(driver, login, password)

        # Ждем главную страницу и кнопку "Войти/оформить"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)

        # Проверяем, что на главной странице появилась кнопка "Оформить заказ"
        assert helpers.check_order_button(driver)


    def test_auth_from_pass_recover_page(self, get_driver):
        ''' Проверка входа через ссылку "Войти" на странице восстановления пароля '''
        # Открываем окно веб-драйвера и страницу регистрации
        driver = get_driver
        helpers.open_reg_window(driver)

        # Выполняем регистрацию нового пользователя, сохраняем логин и пароль
        login, password = helpers.register_new_user(driver)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Открываем страницу восстановления пароля и ждем появления ссылки "Войти"
        driver.get(url.RECOVER_PAGE_URL)

        helpers.wait_url(driver, url.RECOVER_PAGE_URL)
        helpers.wait_element(driver, loc.RECOVER_PAGE_LINK)

        # Кликаем по ссылке "Войти"
        helpers.click_element(driver, loc.RECOVER_PAGE_LINK)

        # Ждем страницу авторизации и кнопку "Войти"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)
        helpers.wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

        # Выполняем авторизацию
        helpers.sign_in(driver, login, password)

        # Ждем главную страницу и кнопку "Войти/оформить"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)

        # Проверяем, что на главной странице появилась кнопка "Оформить заказ"
        assert helpers.check_order_button(driver)

