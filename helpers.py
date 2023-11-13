from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from random import randint
from selenium import webdriver
import pytest



import data
from urls import URLS as url
from locators import Locators as loc


def get_user_name():
    ''' Генерация пароля '''
    return data.DATA.USER_NAME


def gen_login():
    ''' Генерация email по шаблону '''
    code = randint(10000, 99999)
    email = f"svetlana_ananina_2_{code}@yandex.ru"
    return email


def gen_password():
    ''' Генерация пароля '''
    return data.DATA.USER_PASSWORD


def gen_invalid_password():
    ''' Генерация неверного пароля '''
    return data.DATA.INVALID_PASSWORD


def set_value(driver, locator, value):
    driver.find_element(*locator).send_keys(value)


def wait_element(driver, locator):
    WebDriverWait(driver, 5).until(
        expected_conditions.presence_of_element_located(locator) and
        expected_conditions.visibility_of_element_located(locator))


def wait_url(driver, url_text):
    return WebDriverWait(driver, 5).until(expected_conditions.url_to_be(url_text))


def wait_url_changes(driver, url_text):
    return WebDriverWait(driver, 5).until(expected_conditions.url_changes(url_text))


def click_element(driver, locator):
    driver.find_element(*locator).click()


def find_element(driver, locator):
    return driver.find_element(*locator)


def find_elements(driver, locator):
    return driver.find_elements(*locator)


def is_active(driver, locator):
    ''' Вспомогательная функция.
        Получает:   driver - ссылка на веб-драйвер,
                    locator - строка поиска с атрибутом "class" ("".//body//main/section[1]/div/div[1]"" - Раздел Булки в Кондиструкторе бургеров)
        Получает название класса выбранного элемента конструктора и проверяет наличие в нем подстроки "current".
        Возвращает True/False
    '''

    return "current" in driver.find_element(*locator).get_attribute("class")


def open_reg_window(driver):
    """ Открываем страницу регистрации """
    driver.get(url.REG_PAGE_URL)
    return driver


def open_main_window(driver):
    """ Открываем главную страницу """
    driver.get(url.MAIN_PAGE_URL)
    return driver


#def register_new_user(driver, name=get_user_name(), login=gen_login(), password=gen_password()):
def register_new_user(driver, name=None, login=None, password=None):
    ''' Функция регистрации, выполняется перед тестами на авторизацию и Личный кабинет.
    Открывает страницу регистрации.
    Выполняет регистрацию.
    Возвращает ссылку на веб-драйвер; логин и пароль
    '''
    # Открываем страницу регистрации
    open_reg_window(driver)

    # Ждем открытия окна регистрации и появления кнопки 'Зарегистрироваться'
    wait_url(driver, url.REG_PAGE_URL)
    wait_element(driver, loc.REG_BUTTON)

    # Вводим данные в поля
    if name == None:
        name = get_user_name()
    if login == None:
        login = gen_login()
    if password == None:
        password = gen_password()
    set_value(driver, loc.USER_NAME_INPUT, name)
    set_value(driver, loc.USER_EMAIL_INPUT, login)
    set_value(driver, loc.USER_PASSWORD_INPUT, password)

    # Кликаем кнопку "Зарегистрироваться"
    click_element(driver, loc.REG_BUTTON)

    return login, password


def sign_in(driver, login, password):
    ''' Вспомогательная функция. Выполняет авторизацию на странице авторизации '''
    # Вводим логин и пароль, кликаем кнопку "Войти"
    set_value(driver, loc.AUTH_PAGE_LOGIN_FIELD, login)
    set_value(driver, loc.AUTH_PAGE_PASSWORD_FIELD, password)
    click_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

    return driver


def check_order_button(driver):
    """ Проверяем, что на главной странице появилась кнопка "Оформить заказ" """
    elements = find_elements(driver, loc.MAIN_PAGE_ORDER_BUTTON)
    if len(elements) == 1:
        return True
    else:
        return False

def register_and_login(driver):
    """ Вспомогательная функция: выполняет регистрацию и авторизацию нового пользователя.
        Выполняется в начале тестов Личного кабинета
    """
    # Вызываем функцию регистрации
    login, password = register_new_user(driver)

    # Ждем страницу авторизации и кнопку "Войти"
    wait_url(driver, url.AUTH_PAGE_URL)
    wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

    # Открываем главную страницу
    open_main_window(driver)

    # Ждем, когда откроется главная страница и появится кнопка "Войти в аккаунт"
    wait_url(driver, url.MAIN_PAGE_URL)
    wait_element(driver, loc.MAIN_PAGE_LOGIN_BUTTON)

    # Кликаем кнопку "Войти в аккаунт"
    click_element(driver, loc.MAIN_PAGE_LOGIN_BUTTON)

    # Ждем страницу авторизации и кнопку "Войти"
    wait_url(driver, url.AUTH_PAGE_URL)
    wait_element(driver, loc.AUTH_PAGE_LOGIN_BUTTON)

    # Вызываем функцию авторизации
    sign_in(driver, login, password)

    # Ждем Главную страницу и кнопку "Оформить заказ"/"Войти в аккаунт"
    wait_url(driver, url.MAIN_PAGE_URL)
    wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)

    return driver

