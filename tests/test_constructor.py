import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import (
    BUNS_TAB, SAUCES_TAB, FILLINGS_TAB, CONSTRUCTOR_ELEMENT
)
from urls import URLs

class TestConstructorFunctionality:
    """Тесты для проверки переходов в разделы конструктора"""
    @pytest.mark.parametrize("driver", [URLs.BASE_URL], indirect=True)
    def test_go_to_sauces_tab(self, driver):
        """Проверка перехода в раздел 'Соусы'."""
        wait = WebDriverWait(driver, 30)
        # Открываем страницу конструктора
        driver.get(URLs.BASE_URL)
        # Переход в конструктор
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_ELEMENT)).click()
        # Ожидаем, что раздел "Соусы" доступен и переходим в него
        wait.until(EC.element_to_be_clickable(SAUCES_TAB)).click()
        # Проверяем, что мы на странице "Соусы"
        assert "Соусы" in driver.page_source, "Не удалось перейти в раздел 'Соусы'"

    @pytest.mark.parametrize("driver", [URLs.BASE_URL], indirect=True)
    def test_go_to_buns_tab(self, driver):
        """Проверка того, что раздел 'Булки' выбран по умолчанию."""
        wait = WebDriverWait(driver, 30)
        # Открываем страницу конструктора
        driver.get(URLs.BASE_URL)
        # Переход в конструктор
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_ELEMENT)).click()
        # Проверяем, что раздел "Булки" активен (выбран по умолчанию)
        buns_tab = wait.until(EC.visibility_of_element_located(BUNS_TAB))
        assert "tab_tab_type_current__2BEPc" in buns_tab.get_attribute("class"), \
            "Раздел 'Булки' не выбран по умолчанию"

    @pytest.mark.parametrize("driver", [URLs.BASE_URL], indirect=True)
    def test_go_to_fillings_tab(self, driver):
        """Проверка перехода в раздел 'Начинки'."""
        wait = WebDriverWait(driver, 30)
        # Открываем страницу конструктора
        driver.get(URLs.BASE_URL)
        # Переход в конструктор
        wait.until(EC.element_to_be_clickable(CONSTRUCTOR_ELEMENT)).click()
        # Ожидаем, что раздел "Начинки" доступен и переходим в него
        wait.until(EC.element_to_be_clickable(FILLINGS_TAB)).click()
        # Проверяем, что мы на странице "Начинки"
        assert "Начинки" in driver.page_source, "Не удалось перейти в раздел 'Начинки'"