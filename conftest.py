from random import randint
import pytest
from selenium import webdriver

import data
from urls import URLS as url
from locators import Locators as loc
import helpers


@pytest.fixture
def get_user_name():
    ''' Генерация пароля '''
    return data.DATA.USER_NAME


@pytest.fixture
def gen_login():
    ''' Генерация email по шаблону '''
    code = randint(10000, 99999)
    email = f"svetlana_ananina_2_{code}@yandex.ru"
    return email


@pytest.fixture
def gen_password():
    ''' Генерация пароля '''
    return data.DATA.USER_PASSWORD


@pytest.fixture
def gen_invalid_password():
    ''' Генерация неверного пароля '''
    return data.DATA.INVALID_PASSWORD


@pytest.fixture
def open_reg_window():
    # Открываем страницу регистрации
    driver = webdriver.Chrome()
    driver.get(url.REG_PAGE_URL)
    return driver


@pytest.fixture
def open_main_window():
    # Открываем главную страницу
    driver = webdriver.Chrome()
    driver.get(url.MAIN_PAGE_URL)
    yield driver

    # Закрываем драйвер по окончании использования фикстуры
    driver.quit()


@pytest.fixture
def register_new_user(open_reg_window, gen_login, gen_password, get_user_name):
    ''' Функция регистрации, выполняется перед тестами на авторизацию и Личный кабинет.
        Открывает окно веб-драйвера.
        Выполняет регистрацию.
        #Сохраняет ссылку на веб-драйвер, логин и пароль в переменной AuthData::data.reg_data.
        Возвращает ссылку на веб-драйвер; логин и пароль в переменной AuthData::data.reg_data
    '''
    driver = open_reg_window        # Функция-фикстура открывает окно веб-драйвера и страницу регистрации

    # Получаем данные для регистрации и сохраняем их в объект класса AuthData: data.reg_data
    name = get_user_name
    login = gen_login               # Генерирует логин по шаблону
    password = gen_password         # Генерирует пароль

    reg_data = data.AuthData()      # Создаем объект с данными сессии
    reg_data.driver = driver
    reg_data.login = login
    reg_data.password = password
    reg_data.registration_flg = False

    # Ждем появления кнопки 'Зарегистрироваться'
    helpers.wait_element(driver, loc.REG_BUTTON)

    # Вводим данные в поля и кликаем кнопку
    helpers.set_value(driver, loc.USER_NAME_INPUT, name)
    helpers.set_value(driver, loc.USER_EMAIL_INPUT, login)
    helpers.set_value(driver, loc.USER_PASSWORD_INPUT, password)

    helpers.click_element(driver, loc.REG_BUTTON)

    # Проверяем, что произошел переход на страницу авторизации и появится кнопка "Войти"
    helpers.wait_url(driver, url.AUTH_PAGE_URL)
    helpers.wait_element(driver, loc.LOGIN_BUTTON)
    if driver.current_url != url.AUTH_PAGE_URL:
        message = 'Ошибка регистрации: не удалось зарегистрироваться login={}, password={}'.format(login, password)
        raise Exception(message)
    reg_data.registration_flg = True

    yield driver, reg_data
    # Закрываем драйвер по окончании использования фикстуры
    driver.quit()

