import random
import string


def generate_login(name="test", surname="testov", cohort="1999"):
    """Уникальный email в формате: имя + фамилия + когорта + 3 цифры @ домен."""
    digits = f"{random.randint(100, 999)}"
    return f"{name}{surname}{cohort}{digits}@yandex.ru"


def generate_password(length=8):
    """Пароль длиной не менее 6 символов."""
    if length < 6:
        length = 6
    chars = string.ascii_letters + string.digits
    return "".join(random.choices(chars, k=length))