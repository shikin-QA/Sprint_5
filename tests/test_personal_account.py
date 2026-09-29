from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *

TIMEOUT = 30


def login(driver, email, password):
    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    ).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_BUTTON)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(ORDER_BUTTON)
    )


class TestPersonalAccount:

    def test_go_to_personal_account(self, driver, registered_user):
        email, password = registered_user
        login(driver, email, password)

        driver.get(BASE_URL.rstrip("/") + "/account")
        logout = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        )
        assert logout.is_displayed()

    def test_logout(self, driver, registered_user):
        email, password = registered_user
        login(driver, email, password)

        driver.get(BASE_URL.rstrip("/") + "/account")
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(LOGOUT_BUTTON)
        ).click()
        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )
        assert "/login" in driver.current_url

    def test_go_to_constructor_from_account(self, driver, registered_user):
        email, password = registered_user
        login(driver, email, password)

        driver.get(BASE_URL.rstrip("/") + "/account")
        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        )
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(CONSTRUCTOR_LINK)
        ).click()
        order = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(ORDER_BUTTON)
        )
        assert order.is_displayed()

    def test_go_to_constructor_by_logo(self, driver, registered_user):
        email, password = registered_user
        login(driver, email, password)

        driver.get(BASE_URL.rstrip("/") + "/account")
        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(LOGOUT_BUTTON)
        )
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(LOGO)
        ).click()
        order = WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(ORDER_BUTTON)
        )
        assert order.is_displayed()