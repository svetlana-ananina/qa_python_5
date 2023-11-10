from urls import URLS as url
from locators import Locators as loc
import helpers


class TestProfilePage:
    """ Функция-фикстура "register_new_user" выполняется в начале каждого теста:
        Открывает окно веб-драйвера.
        Выполняет регистрацию.
        Возвращает ссылку на веб-драйвер, логин и пароль в переменной AuthData::reg_data
    """

    def test_open_profile_from_main_page(self, register_new_user):
        """ Проверка входа в профиль """
        driver, reg_data = register_new_user                        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        driver.get(url.AUTH_PAGE_URL)                               # Открываем страницу авторизации
        assert helpers.sign_in(driver, login, password)             # Выполняем авторизацию

        driver.get(url.MAIN_PAGE_URL)                               # Открываем главную страницу
        helpers.wait_url(driver, url.MAIN_PAGE_URL)                 # Ждем когда откроется главная страница
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)    # и появится ссылка на Личный кабинет
        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)   # Кликаем ссылку на Личный кабинет
        helpers.wait_url(driver, url.PROFILE_PAGE_URL)              # Ждем когда откроется страница Личный кабинет

        assert driver.current_url == url.PROFILE_PAGE_URL


    def test_click_logo_from_profile_page(self, register_new_user):
        """ Проверка выхода из Личного кабинета по клику на логотип """
        driver, reg_data = register_new_user                        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        driver.get(url.AUTH_PAGE_URL)                               # Открываем страницу авторизации
        assert helpers.sign_in(driver, login, password)             # Выполняем авторизацию

        driver.get(url.MAIN_PAGE_URL)                               # Открываем главную страницу
        helpers.wait_url(driver, url.MAIN_PAGE_URL)                 # Ждем когда откроется Главная страница
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)    # и появится ссылка "Личный кабинет"

        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)   # Кликаем "Личный кабинет"
        helpers.wait_url(driver, url.PROFILE_PAGE_URL)              # Ждем когда откроется страница Личный кабинет

        assert driver.current_url == url.PROFILE_PAGE_URL

        helpers.wait_element(driver, loc.PROFILE_PAGE_LOGO_LINK)    # Ждем когда появится ссылка на Лого
        helpers.click_element(driver, loc.PROFILE_PAGE_LOGO_LINK)   # Кликаем на Лого
        helpers.wait_url(driver, url.MAIN_PAGE_URL)                 # Ждем когда откроется Главная страница

        assert driver.current_url == url.MAIN_PAGE_URL


    def test_click_constructor_from_profile_page(self, register_new_user):
        """ Проверка выхода из Личного кабинета по клику на Конструктор """
        driver, reg_data = register_new_user                        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        driver.get(url.AUTH_PAGE_URL)                               # Открываем страницу авторизации
        assert helpers.sign_in(driver, login, password)             # Выполняем авторизацию

        driver.get(url.MAIN_PAGE_URL)                               # Открываем главную страницу
        helpers.wait_url(driver, url.MAIN_PAGE_URL)                 # Ждем когда откроется Главная страница
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)    # и появится ссылка "Личный кабинет"

        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)   # Кликаем "Личный кабинет"
        helpers.wait_url(driver, url.PROFILE_PAGE_URL)              # Ждем когда откроется страница Личный кабинет
        assert driver.current_url == url.PROFILE_PAGE_URL

        helpers.wait_element(driver, loc.PROFILE_PAGE_CONSTRUCTOR_LINK)    # Ждем когда появится ссылка на Конструктор
        helpers.click_element(driver, loc.PROFILE_PAGE_CONSTRUCTOR_LINK)   # Кликаем на Конструктор
        helpers.wait_url(driver, url.MAIN_PAGE_URL)                        # Ждем когда откроется Главная страница

        assert driver.current_url == url.MAIN_PAGE_URL


    def test_sign_out_from_profile_page(self, register_new_user):
        """ Проверка выхода из аккаунта по кнопке 'Выйти' в Личном кабинете """
        driver, reg_data = register_new_user                        # Выполняем регистрацию нового пользователя
        login = reg_data.login
        password = reg_data.password

        driver.get(url.AUTH_PAGE_URL)                               # Открываем страницу авторизации
        assert helpers.sign_in(driver, login, password)             # Выполняем авторизацию

        driver.get(url.MAIN_PAGE_URL)                               # Открываем главную страницу
        helpers.wait_url(driver, url.MAIN_PAGE_URL)                 # Ждем когда откроется Главная страница
        helpers.wait_element(driver, loc.MAIN_PAGE_PROFILE_LINK)    # и появится ссылка "Личный кабинет"

        helpers.click_element(driver, loc.MAIN_PAGE_PROFILE_LINK)   # Кликаем "Личный кабинет"
        helpers.wait_url(driver, url.PROFILE_PAGE_URL)              # Ждем когда откроется страница Личный кабинет
        assert driver.current_url == url.PROFILE_PAGE_URL

        helpers.wait_element(driver, loc.PROFILE_PAGE_EXIT_BUTTON)  # Ждем когда появится кнопка "Выход"
        helpers.click_element(driver, loc.PROFILE_PAGE_EXIT_BUTTON) # Кликаем кнопку "Выход"
        helpers.wait_url(driver, url.AUTH_PAGE_URL)                 # Ждем когда откроется страница авторизации

        assert driver.current_url == url.AUTH_PAGE_URL

