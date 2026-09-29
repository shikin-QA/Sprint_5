from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *

TIMEOUT = 30


class TestConstructor:

    def test_go_to_buns_section(self, driver):
        driver.get(BASE_URL)
        # Сначала переключаемся на «Соусы», затем обратно на «Булки»
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(SAUCES_TAB)
        ).click()
        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(ACTIVE_SAUCES_TAB)
        )
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(BUNS_TAB)
        ).click()
        active_tab = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(ACTIVE_BUNS_TAB)
        )
        assert active_tab.is_displayed()
        assert "Булки" in active_tab.text

    def test_go_to_sauces_section(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(SAUCES_TAB)
        ).click()
        active_tab = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(ACTIVE_SAUCES_TAB)
        )
        assert active_tab.is_displayed()
        assert "Соусы" in active_tab.text

    def test_go_to_fillings_section(self, driver):
        driver.get(BASE_URL)
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(FILLINGS_TAB)
        ).click()
        active_tab = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(ACTIVE_FILLINGS_TAB)
        )
        assert active_tab.is_displayed()
        assert "Начинки" in active_tab.text