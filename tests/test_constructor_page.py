from locators import Locators as loc
import helpers


class TestConstructorPage:

    def test_ingredients_fillings(self, get_driver):
        """ Выбор раздела Начинки """
        # Открываем окно веб-драйвера и Главную страницу
        driver = get_driver
        helpers.open_main_window(driver)

        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)          # Ждем кнопку "Войти в аккаунт"/"Оформить заказ"
        helpers.click_element(driver, loc.MAIN_PAGE_FILLINGS_TAB)       # Кликаем вкладку Начинки

        assert helpers.is_active(driver, loc.MAIN_PAGE_FILLINGS_CLASS)  # Получаем статус вкладки Булки


    def test_ingredients_souces(self, get_driver):
        """ Выбор раздела Соусы """
        # Открываем окно веб-драйвера и Главную страницу
        driver = get_driver
        helpers.open_main_window(driver)

        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)          # Ждем кнопку "Войти в аккаунт"/"Оформить заказ"
        helpers.click_element(driver, loc.MAIN_PAGE_SOUCES_TAB)         # Кликаем вкладку Соусы

        assert helpers.is_active(driver, loc.MAIN_PAGE_SOUCES_CLASS)  # Получаем статус вкладки Булки


    def test_ingredients_rolls(self, get_driver):
        """ Выбор раздела Булки """
        # Открываем окно веб-драйвера и Главную страницу
        driver = get_driver
        helpers.open_main_window(driver)

        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)          # Ждем кнопку "Войти в аккаунт"/"Оформить заказ"
        helpers.click_element(driver, loc.MAIN_PAGE_SOUCES_TAB)         # Кликаем вкладку Соусы

        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)          # Ждем кнопку "Войти в аккаунт"/"Оформить заказ"
        helpers.click_element(driver, loc.MAIN_PAGE_ROLLS_TAB)          # Кликаем вкладку Булки

        helpers.wait_element(driver, loc.MAIN_PAGE_ANY_BUTTON)          # Ждем кнопку "Войти в аккаунт"/"Оформить заказ"
        assert helpers.is_active(driver, loc.MAIN_PAGE_ROLLS_CLASS)     # Проверяем статус вкладки Булки

