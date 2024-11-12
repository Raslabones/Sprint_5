import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import (
    PERSONAL_ACCOUNT_BUTTON, PLACE_ORDER_BUTTON, MAIN_HEADER, LOGO_ELEMENT, LOGOUT_BUTTON
)
from urls import URLs
class TestLoginFunctionality:
    """Тесты для проверки различных сценариев входа и переходов после входа"""
    @pytest.mark.parametrize("authorized_user", [URLs.BASE_URL], indirect=True)
    def test_login_via_main_page_button(self, authorized_user):
        """Проверка успешного входа через кнопку 'Войти в аккаунт' на главной странице."""
        wait = WebDriverWait(authorized_user, 30)
        assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), \
            "Кнопка 'Оформить заказ' не найдена, вход не удался"

    @pytest.mark.parametrize("authorized_user", [URLs.BASE_URL], indirect=True)
    def test_go_to_personal_account_after_login(self, authorized_user):
        """Проверка перехода в 'Личный кабинет' после авторизации."""
        wait = WebDriverWait(authorized_user, 30)
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.url_to_be(URLs.ACCOUNT_PAGE))
        assert authorized_user.current_url == URLs.ACCOUNT_PAGE, \
            f"Ожидался переход на страницу личного кабинета, но текущий URL {authorized_user.current_url}"

    @pytest.mark.parametrize("authorized_user", [URLs.BASE_URL], indirect=True)
    def test_logout_via_personal_account(self, authorized_user):
        """Проверка выхода через Личный кабинет и редиректа на страницу входа."""
        wait = WebDriverWait(authorized_user, 30)
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LOGOUT_BUTTON)).click()
        wait.until(EC.url_to_be(URLs.LOGIN_PAGE))
        assert authorized_user.current_url == URLs.LOGIN_PAGE, \
            f"Ожидался редирект на страницу входа, но текущий URL: {authorized_user.current_url}"

    @pytest.mark.parametrize("authorized_user", [URLs.BASE_URL], indirect=True)
    def test_click_logo_after_login(self, authorized_user):
        """Проверка клика на логотип Stellar Burgers после авторизации."""
        wait = WebDriverWait(authorized_user, 30)
        wait.until(EC.element_to_be_clickable(PERSONAL_ACCOUNT_BUTTON)).click()
        wait.until(EC.element_to_be_clickable(LOGO_ELEMENT)).click()
        main_header = wait.until(EC.visibility_of_element_located(MAIN_HEADER))
        assert main_header.is_displayed(), "Заголовок главной страницы не найден."