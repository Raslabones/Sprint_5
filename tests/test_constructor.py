import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import (
    BUNS_TAB, SAUCES_TAB, FILLINGS_TAB, CONSTRUCTOR_ELEMENT, PLACE_ORDER_BUTTON
)
from urls import URLs

class TestTabsNavigation:
    def test_click_buns_tab_and_verify_class(self, authorized_user):
        """Проверка клика на вкладку 'Булки' и проверки класса после авторизации."""
        wait = WebDriverWait(authorized_user, 30)
        assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), \
            "Кнопка 'Оформить заказ' не найдена, вход не удался"

        expected_class_fragment = "tab_tab_type_current__2BEPc"
        authorized_user.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(BUNS_TAB)))
        assert expected_class_fragment in authorized_user.find_element(*BUNS_TAB).get_attribute("class"), \
            "Класс вкладки 'Булки' не соответствует ожидаемому."

    def test_click_sauces_tab_and_verify_class(self, authorized_user):
        """Проверка клика на вкладку 'Соусы' и проверки класса после авторизации."""
        wait = WebDriverWait(authorized_user, 30)
        assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), \
            "Кнопка 'Оформить заказ' не найдена, вход не удался"

        expected_class_fragment = "tab_tab_type_current__2BEPc"
        authorized_user.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(SAUCES_TAB)))
        assert expected_class_fragment in authorized_user.find_element(*SAUCES_TAB).get_attribute("class"), \
            "Класс вкладки 'Соусы' не соответствует ожидаемому."

    def test_click_fillings_tab_and_verify_class(self, authorized_user):
        """Проверка клика на вкладку 'Начинки' и проверки класса после авторизации."""
        wait = WebDriverWait(authorized_user, 30)
        assert wait.until(EC.visibility_of_element_located(PLACE_ORDER_BUTTON)), \
            "Кнопка 'Оформить заказ' не найдена, вход не удался"

        expected_class_fragment = "tab_tab_type_current__2BEPc"
        authorized_user.execute_script("arguments[0].click();", wait.until(EC.element_to_be_clickable(FILLINGS_TAB)))
        assert expected_class_fragment in authorized_user.find_element(*FILLINGS_TAB).get_attribute("class"), \
            "Класс вкладки 'Начинки' не соответствует ожидаемому."
