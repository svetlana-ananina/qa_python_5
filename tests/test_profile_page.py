from urls import URLS as url
from locators import Locators as loc
import helpers
from selenium import webdriver
import pytest


@pytest.mark.usefixtures("get_driver")
class TestProfilePage:

    def test_open_profile_from_main_page(self, get_driver):
        """ Проверка входа в профиль """
        # Выполняем регистрацию и авторизацию нового пользователя
        driver = helpers.register_and_login(get_driver)

        # Открываем главную страницу
        driver.get(url.MAIN_PAGE_URL)

        # Ждем, когда откроется главная страница и появится кнопка "Личный кабинет"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Кликаем кнопку "Личный кабинет"
        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Ждем когда откроется страница Личный кабинет
        helpers.wait_url(driver, url.PROFILE_PAGE_URL)

        # Проверяем, что открылась страница "Личный кабинет"
        assert driver.current_url == url.PROFILE_PAGE_URL


    def test_click_logo_from_profile_page(self, get_driver):
        """ Проверка выхода из Личного кабинета по клику на логотип """
        # Выполняем регистрацию и авторизацию нового пользователя
        driver = helpers.register_and_login(get_driver)

        # Открываем главную страницу
        driver.get(url.MAIN_PAGE_URL)

        # Ждем, когда откроется главная страница и появится кнопка "Личный кабинет"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Кликаем кнопку "Личный кабинет"
        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Ждем когда откроется страница Личный кабинет
        helpers.wait_url(driver, url.PROFILE_PAGE_URL)

        # Проверяем, что открылась страница "Личный кабинет"
        assert driver.current_url == url.PROFILE_PAGE_URL

        # Ждем когда полностью откроется страница Личный кабинет
        helpers.wait_element(driver, loc.PROFILE_PAGE_SAVE_BUTTON)

        # Ждем когда появится ссылка на Лого и кликаем на Лого
        helpers.wait_element(driver, loc.PROFILE_PAGE_LOGO_LINK)
        helpers.click_element(driver, loc.PROFILE_PAGE_LOGO_LINK)

        # Ждем когда откроется Главная страница
        helpers.wait_url(driver, url.MAIN_PAGE_URL)

        # Проверяем, что открылась Главная страница
        assert driver.current_url == url.MAIN_PAGE_URL


    def test_click_constructor_from_profile_page(self, get_driver):
        """ Проверка выхода из Личного кабинета по клику на Конструктор """
        # Выполняем регистрацию и авторизацию нового пользователя
        driver = helpers.register_and_login(get_driver)

        # Открываем главную страницу
        driver.get(url.MAIN_PAGE_URL)

        # Ждем, когда откроется главная страница и появится кнопка "Личный кабинет"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Кликаем кнопку "Личный кабинет"
        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Ждем когда откроется страница Личный кабинет
        helpers.wait_url(driver, url.PROFILE_PAGE_URL)

        # Проверяем, что открылась страница "Личный кабинет"
        assert driver.current_url == url.PROFILE_PAGE_URL

        # Ждем когда полностью откроется страница Личный кабинет
        helpers.wait_element(driver, loc.PROFILE_PAGE_SAVE_BUTTON)

        # Ждем когда появится ссылка на Конструктор и кликаем на него
        helpers.wait_element(driver, loc.PROFILE_PAGE_CONSTRUCTOR_LINK)
        helpers.click_element(driver, loc.PROFILE_PAGE_CONSTRUCTOR_LINK)

        # Ждем когда откроется Главная страница
        helpers.wait_url(driver, url.MAIN_PAGE_URL)

        # Проверяем, что открылась Главная страница
        assert driver.current_url == url.MAIN_PAGE_URL


    def test_sign_out_from_profile_page(self, get_driver):
        """ Проверка выхода из аккаунта по кнопке 'Выйти' в Личном кабинете """
        # Выполняем регистрацию и авторизацию нового пользователя
        driver = helpers.register_and_login(get_driver)

        # Открываем главную страницу
        driver.get(url.MAIN_PAGE_URL)

        # Ждем, когда откроется главная страница и появится кнопка "Личный кабинет"
        helpers.wait_url(driver, url.MAIN_PAGE_URL)
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Кликаем кнопку "Личный кабинет"
        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)

        # Ждем когда откроется страница Личный кабинет
        helpers.wait_url(driver, url.PROFILE_PAGE_URL)

        # Проверяем, что открылась страница "Личный кабинет"
        assert driver.current_url == url.PROFILE_PAGE_URL

        # Ждем когда появится кнопка "Выход" и кликаем ее
        helpers.wait_element(driver, loc.PROFILE_PAGE_EXIT_BUTTON)
        helpers.click_element(driver, loc.PROFILE_PAGE_EXIT_BUTTON)

        # Ждем когда откроется страница авторизации
        helpers.wait_url(driver, url.AUTH_PAGE_URL)

        # Проверяем, что открылась страница авторизации
        assert driver.current_url == url.AUTH_PAGE_URL

