from selenium.webdriver.common.by import By


class Locators:

    # Форма регистрации
    REG_FORM = (By.XPATH, ".//form")                                                        # Форма регистрации
    USER_NAME_INPUT = (By.XPATH, "(.//input[@name='name'])[1]")                             # Поле ввода имени
    USER_EMAIL_INPUT = (By.XPATH, "(.//input[@name='name'])[2]")                            # Поле ввода логина
    USER_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")                            # Поле ввода пароля
    REG_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")                       # Кнопка "Зарегистрироваться"
    REG_PAGE_LOGIN_LINK = (By.XPATH, ".//a[text()='Войти']")                                # Ссылка "Войти" на странице регистрации
    REG_PAGE_ERROR_MESSAGE = (By.CLASS_NAME, "input__error")
    # Главная страница
    MAIN_PAGE_MAIN_SECTION = (By.XPATH, ".//body//main")                                    # Раздел main на главной странице
    MAIN_PAGE_BODY = (By.XPATH, ".//body")                                                  # Раздел body на главной странице
    # Кнопка "Войти в аккаунт"/"Оформить заказ" на Главной странице
    MAIN_PAGE_LOGIN_BUTTON = (By.XPATH, ".//body//main//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт" на главной странице
    MAIN_PAGE_ORDER_BUTTON = (By.XPATH, ".//body//main//button[text()='Оформить заказ']")   # Кнопка "Оформить заказ" на главной странице
    MAIN_PAGE_ANY_BUTTON = (By.XPATH, ".//body//main//button")                              # Кнопка "Войти в аккаунт"/"Оформить заказ" на главной странице
    # Ссылка на Личный кабинет на Главной странице
    MAIN_PAGE_PROFILE_TEXT = (By.XPATH, ".//body//header//p[text()='Личный Кабинет']")      # Текст кнопки "Личный Кабинет" на главной странице
    MAIN_PAGE_PROFILE_LINK = (By.XPATH, ".//body//header//a[@href='/account']")             # Ссылка "Личный Кабинет" на главной странице
    # Раздел Конструктор
    MAIN_PAGE_ROLLS_TAB = (By.XPATH, ".//body//main//span[text()='Булки']")                 # Вкладка Булки
    MAIN_PAGE_ROLLS_CLASS = (By.XPATH, ".//body//main/section[1]/div/div[1]")
    MAIN_PAGE_SOUCES_TAB = (By.XPATH, ".//body//main//span[text()='Соусы']")                # Вкладка Соусы
    MAIN_PAGE_SOUCES_CLASS = (By.XPATH, ".//body//main/section[1]/div/div[2]")
    MAIN_PAGE_FILLINGS_TAB = (By.XPATH, ".//body//main//span[text()='Начинки']")            # Вкладка Начинки
    MAIN_PAGE_FILLINGS_CLASS = (By.XPATH, ".//body//main/section[1]/div/div[3]")
    MAIN_PAGE_ALL_TABS = (By.XPATH, ".//body//main/section[1]/div/div")                     # Все вкладки в Конструкторе
    # Личный кабинет
    PROFILE_PAGE_LOGO_LINK = (By.XPATH, ".//body//header//div/a[@href='/']")                # Ссылка на Лого на странице Личный кабинет
    PROFILE_PAGE_CONSTRUCTOR_LINK = (By.XPATH, ".//body//header//p[text()='Конструктор']")  # Сссылка на Конструктор на странице Личный кабинет
    PROFILE_PAGE_SAVE_BUTTON = (By.XPATH, ".//body//main//button[text()='Сохранить']")      # Кнопка "Сохранить" на странице Личный кабинет
    PROFILE_PAGE_EXIT_BUTTON = (By.XPATH, ".//body//main//button[text()='Выход']")          # Кнопка "Выход" на странице Личный кабинет
    # Форма авторизации
    AUTH_PAGE_LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")                        # Кнопка "Войти" на странице авторизации
    AUTH_PAGE_LOGIN_FIELD = (By.XPATH, ".//input[@name='name']")                            # Поле ввода логина
    AUTH_PAGE_PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")                       # Поле ввода пароля
    AUTH_FORM = (By.XPATH, ".//main//form")                                                 # Форма ввода на странице авторизации
    # Форма восстановления пароля
    RECOVER_PAGE_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")                    # Кнопка "Восстановить" на странице восстановления пароля
    RECOVER_PAGE_LINK = (By.XPATH, ".//a[text()='Войти']")                                  # Ссылка "Войти" на странице восстановления пароля
