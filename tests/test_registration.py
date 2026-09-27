import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_login, generate_password
from locators import *

TIMEOUT = 30


def test_successful_registration(driver):
    email = generate_login()
    password = generate_password()

    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(REGISTER_LINK)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(REGISTER_NAME_INPUT)
    ).send_keys("Test")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(REGISTER_BUTTON)
    ).click()

    time.sleep(2)
    driver.get(BASE_URL.rstrip("/") + "/login")
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    )
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_BUTTON)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(ORDER_BUTTON)
    )
    assert driver.find_element(*ORDER_BUTTON).is_displayed()


def test_registration_with_short_password(driver):
    email = generate_login()
    password = "12345"

    driver.get(BASE_URL)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGIN_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(REGISTER_LINK)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(REGISTER_NAME_INPUT)
    ).send_keys("Test")
    driver.find_element(*REGISTER_EMAIL_INPUT).send_keys(email)
    driver.find_element(*REGISTER_PASSWORD_INPUT).send_keys(password)
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(REGISTER_BUTTON)
    ).click()

    error = WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(PASSWORD_ERROR)
    )
    assert error.text == "Некорректный пароль"