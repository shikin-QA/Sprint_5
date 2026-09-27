from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import *

TIMEOUT = 30


def login(driver, email, password):
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


def test_login_from_main_page(driver, registered_user):
    email, password = registered_user
    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_ACCOUNT_BUTTON)
    ).click()
    login(driver, email, password)
    assert driver.find_element(*ORDER_BUTTON).is_displayed()


def test_login_from_personal_account(driver, registered_user):
    email, password = registered_user
    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(PERSONAL_ACCOUNT_LINK)
    ).click()
    login(driver, email, password)
    assert driver.find_element(*ORDER_BUTTON).is_displayed()


def test_login_from_registration_form(driver, registered_user):
    email, password = registered_user
    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(REGISTER_LINK)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_LINK)
    ).click()
    login(driver, email, password)
    assert driver.find_element(*ORDER_BUTTON).is_displayed()


def test_login_from_forgot_password_form(driver, registered_user):
    email, password = registered_user
    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(FORGOT_PASSWORD_LINK)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_LINK)
    ).click()
    login(driver, email, password)
    assert driver.find_element(*ORDER_BUTTON).is_displayed()