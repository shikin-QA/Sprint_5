import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from generators import generate_login, generate_password
from locators import (
    BASE_URL,
    LOGIN_ACCOUNT_BUTTON,
    REGISTER_LINK,
    REGISTER_NAME_INPUT,
    REGISTER_EMAIL_INPUT,
    REGISTER_PASSWORD_INPUT,
    REGISTER_BUTTON,
    ORDER_BUTTON,
    LOGOUT_BUTTON,
    LOGIN_EMAIL_INPUT,
    LOGIN_PASSWORD_INPUT,
    LOGIN_BUTTON,
)

TIMEOUT = 30


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def registered_user(driver):
    """Регистрирует пользователя, логинится и выходит. Возвращает (email, password)."""
    email = generate_login()
    password = generate_password()

    # 1. Регистрация
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

    # 2. Ждём либо редирект на /login, либо форму входа
    WebDriverWait(driver, TIMEOUT).until(
        EC.any_of(
            EC.url_contains("/login"),
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT),
        )
    )
    if "/login" not in driver.current_url:
        driver.get(BASE_URL.rstrip("/") + "/login")
        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
        )

    # 3. Логин (если уже авторизованы — пропускаем)
    if len(driver.find_elements(*ORDER_BUTTON)) == 0:
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        WebDriverWait(driver, TIMEOUT).until(
            EC.element_to_be_clickable(LOGIN_BUTTON)
        ).click()
        WebDriverWait(driver, TIMEOUT).until(
            EC.visibility_of_element_located(ORDER_BUTTON)
        )

    # 4. Личный кабинет → выйти
    driver.get(BASE_URL.rstrip("/") + "/account")
    WebDriverWait(driver, TIMEOUT).until(
        EC.element_to_be_clickable(LOGOUT_BUTTON)
    ).click()
    WebDriverWait(driver, TIMEOUT).until(
        EC.visibility_of_element_located(LOGIN_EMAIL_INPUT)
    )

    return email, password