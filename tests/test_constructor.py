from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *


def test_constructor_tabs(driver):
    driver.get(BASE_URL)

    driver.find_element(*SAUCES_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ACTIVE_SAUCES_TAB))

    driver.find_element(*FILLINGS_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ACTIVE_FILLINGS_TAB))

    driver.find_element(*BUNS_TAB).click()
    WebDriverWait(driver, 5).until(EC.visibility_of_element_located(ACTIVE_BUNS_TAB))