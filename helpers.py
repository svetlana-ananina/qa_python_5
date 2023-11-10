from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import data
from urls import URLS as url
from locators import Locators as loc
import helpers


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


def sign_in(driver, login, password):
    ''' Вспомогательная функция. Выполняет авторизацию, возвращает True/False
        Предварительно выполнен переход на страницу авторизации/открыта страница авторизации
     '''
    # Открываем страницу авторизации и ждем появления кнопки "Войти"
    helpers.wait_url(driver, url.AUTH_PAGE_URL)
    helpers.wait_element(driver, loc.LOGIN_BUTTON)

    # Вводим логин и пароль, кликаем кнопку "Войти"
    set_value(driver, loc.LOGIN_INPUT, login)
    set_value(driver, loc.PASSWORD_INPUT, password)
    click_element(driver, loc.LOGIN_BUTTON)

    # Ждем, что произошел переход на главную страницу
    helpers.wait_url(driver, url.MAIN_PAGE_URL)

    # Ждем, пока появится кнопка "Войти/оформить"
    helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)

    # Проверяем, что на главной странице появилась кнопка "Оформить заказ" - вместо "Войти в аккаунт"
    elements = helpers.find_elements(driver, loc.MAIN_PAGE_ORDER_BUTTON)
    if len(elements) != 1:
        return False
    else:
        return True

