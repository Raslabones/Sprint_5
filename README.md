Проект автоматизированного тестирования для Stellar Burgers
Этот проект содержит автоматизированные тесты для веб-приложения Stellar Burgers, предназначенные для проверки различных функциональностей сайта.

Описание тестов
Тесты проверяют несколько аспектов работы сайта, включая авторизацию, регистрацию и работу конструктора для сборки бургера.

1. Тесты для авторизации:
test_login_via_main_page_button — Проверка успешного входа через кнопку 'Войти в аккаунт' на главной странице.
test_go_to_personal_account_after_login — Проверка перехода в 'Личный кабинет' после авторизации.
test_logout_via_personal_account — Проверка выхода через Личный кабинет и редиректа на страницу входа.
test_click_logo_after_login — Проверка клика на логотип Stellar Burgers после авторизации.
2. Тесты для регистрации:
test_successful_registration — Проверка успешной регистрации с редиректом на страницу логина.
test_registration_error_password — Проверка ошибки при регистрации с некорректным паролем.
3. Тесты для конструктора:
test_go_to_sauces_tab — Проверка перехода в раздел 'Соусы'.
test_go_to_buns_tab — Проверка того, что раздел 'Булки' выбран по умолчанию.
test_go_to_fillings_tab — Проверка перехода в раздел 'Начинки'.