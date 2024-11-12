import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from user_data import user_email, user_password
from locators import (
    LOGIN_BUTTON_MAIN_PAGE, LOGIN_EMAIL_FIELD, LOGIN_PASSWORD_FIELD, LOGIN_SUBMIT_BUTTON,
    RECOVERY_LOGIN_LINK, LOGIN_LINK_REGISTRATION_FORM, PERSONAL_ACCOUNT_BUTTON
)
from urls import URLs
@pytest.fixture
def driver():
    """Фикстура для инициализации веб-драйвера с явными ожиданиями."""
    driver = webdriver.Chrome()
    driver.wait = WebDriverWait(driver, 30)
    yield driver
    driver.quit()
@pytest.fixture
def authorized_user(request, driver):
    """Фикстура для авторизации пользователя с различными начальными страницами."""
    start_page = request.param if hasattr(request, 'param') else URLs.BASE_URL
    driver.get(start_page)
    wait = WebDriverWait(driver, 30)
    # Переход на страницу в зависимости от начальной
    if start_page == URLs.FORGOT_PASSWORD_PAGE:
        wait.until(EC.element_to_be_clickable(RECOVERY_LOGIN_LINK)).click()
    elif start_page == URLs.REGISTER_PAGE:
        wait.until(EC.element_to_be_clickable(LOGIN_LINK_REGISTRATION_FORM)).click()
    elif start_page == URLs.BASE_URL:
        wait.until(EC.element_to_be_clickable(LOGIN_BUTTON_MAIN_PAGE)).click()
    elif start_page == URLs.ACCOUNT_PAGE:
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
    # Ввод email и пароля для авторизации
    wait.until(EC.visibility_of_element_located(LOGIN_EMAIL_FIELD)).send_keys(user_email)
    wait.until(EC.visibility_of_element_located(LOGIN_PASSWORD_FIELD)).send_keys(user_password)
    # Нажатие на кнопку "Войти"
    wait.until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)).click()
    return driver