import pytest
from selenium import webdriver

import data
from urls import URLS as url
from locators import Locators as loc
import helpers


@pytest.fixture
def get_driver():
    """ Открываем окно веб-драйвера """
    driver = webdriver.Chrome()
    yield driver

    # Закрываем драйвер по окончании использования фикстуры
    driver.quit()

