# Тест-сьют для проверки UI приложения Stellar Burgers

Файлы:
- tests/ - папка с файлами тестов
- tests/test_registration_page.py - тесты на страницу регистрации
- tests/test_authorization_page.py - тесты на страницу авторизации
- tests/test_profile_page.py - тесты на страницу Личный кабинет
- tests/test_constructor_page.py - тесты на страницу Конструктор

- helpers.py - вспомогательные функции
- conftest.py - функции-фикстуры
- locators.py - указатели для поиска элементов DOM
- data.py - другие константы
- urls.py - константы URL-адресов

- .gitignore - файл для проекта в Git/GinHub
- README.md - файл с описанием проекта

Для запуска тестов должны быть установлены пакеты pytest и selenium

Запуск всех тестов выполняется командой:
pytest -v ./tests
