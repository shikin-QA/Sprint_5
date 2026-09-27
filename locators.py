from selenium.webdriver.common.by import By

BASE_URL = "https://stellarburgers.education-services.ru/"

# Главная страница
LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
PERSONAL_ACCOUNT_LINK = (By.XPATH, "//a[contains(@href, '/account')]")  # Ссылка «Личный кабинет» в шапке
CONSTRUCTOR_LINK = (By.XPATH, "//a[contains(., 'Конструктор')]")  # Ссылка «Конструктор»
LOGO = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]/a")  # Логотип Stellar Burgers
ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # Кнопка «Оформить заказ» — признак авторизации

# Форма регистрации
REGISTER_NAME_INPUT = (By.XPATH, "//label[text()='Имя']/..//input")  # Поле «Имя»
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/..//input")  # Поле «Email»
REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/..//input")  # Поле «Пароль»
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # Кнопка «Зарегистрироваться»
REGISTER_LINK = (By.XPATH, "//a[text()='Зарегистрироваться']")  # Ссылка «Зарегистрироваться»
PASSWORD_ERROR = (By.XPATH, "//p[text()='Некорректный пароль']")  # Ошибка о некорректном пароле

# Форма входа
LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/..//input")  # Поле «Email» на странице входа
LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/..//input")  # Поле «Пароль» на странице входа
LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")  # Кнопка «Войти»
LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")  # Ссылка «Войти»
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Восстановить пароль']")  # Ссылка «Восстановить пароль»

# Личный кабинет
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # Кнопка «Выйти»

# Раздел «Конструктор»
BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # Таб «Булки»
SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # Таб «Соусы»
FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # Таб «Начинки»
ACTIVE_BUNS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Булки']")
ACTIVE_SAUCES_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Соусы']")
ACTIVE_FILLINGS_TAB = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]//span[text()='Начинки']")