class DATA:
    # Текст кнопок/элементов
    INVALID_PASS_TEXT = 'Некорректный пароль'  # Текст сообщения о неверном пароле на странице регистрации
    MAIN_PAGE_LOGIN_BUTTON_TEXT = 'Войти в аккаунт'  # Текст кнопки 'Войти в аккаунт' на главной странице
    MAIN_PAGE_ORDER_BUTTON_TEXT = 'Оформить заказ'  # Текст кнопки 'Оформить заказ' на главной странице
    MAIN_PAGE_PROFILE_BUTTON_TEXT = 'Личный Кабинет'  # Текст кнопки 'Личный Кабинет' на главной странице
    RECOVER_PAGE_BUTTON_TEXT = 'Восстановить'  # Текст кнопки "Восстановить" на странице восстановления пароля

    # Константы для регистрации
    USER_NAME = 'Svetlana'
    USER_PASSWORD = '123456'
    INVALID_PASSWORD = '123'


# Класс для передачи регистрационных данных и ссылки на открытое окно браузера
class AuthData:
    def __init__(self):
        self.driver = None
        self.login = None
        self.password = None
        self.registration_flg = False

