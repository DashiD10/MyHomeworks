# Декоратор для проверки пароля

from typing import Callable, Any
import re


def password_checker(func: Callable) -> Callable:
    def wrapper(password: str) -> str:
        if len(password) < 8:
            return "Ошибка: пароль должен содержать минимум 8 символов"

        if not re.search(r"\d", password):
            return "Ошибка: пароль должен содержать хотя бы одну цифру"

        if not re.search(r"[A-Z]", password):
            return "Ошибка: пароль должен содержать хотя бы одну заглавную букву"

        if not re.search(r"[a-z]", password):
            return "Ошибка: пароль должен содержать хотя бы одну строчную букву"

        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "Ошибка: пароль должен содержать хотя бы один специальный символ"

        return func(password)

    return wrapper


@password_checker
def register_user(password: str) -> str:
    return f"Регистрация успешна! Пароль '{password}' соответствует требованиям"


# Примеры использования
print(register_user("слабый пароль"))
print(register_user("Сильный! Пароль123"))


# Декораторы с параметрами

from typing import Callable, Any
import csv
from functools import wraps


def password_validator(
    min_length: int = 8,
    min_uppercase: int = 1,
    min_lowercase: int = 1,
    min_special_chars: int = 1,
) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(username: str, password: str) -> Any:
            if len(password) < min_length:
                raise ValueError(f"Пароль должен быть не менее {min_length} символов")

            if sum(1 for c in password if c.isupper()) < min_uppercase:
                raise ValueError(
                    f"Пароль должен содержать минимум {min_uppercase} заглавных букв"
                )

            if sum(1 for c in password if c.islower()) < min_lowercase:
                raise ValueError(
                    f"Пароль должен содержать минимум {min_lowercase} строчных букв"
                )

            if (
                sum(1 for c in пароль if c in '!@#$%^&*(),.?":{}|<>')
                < min_special_chars
            ):
                raise ValueError(
                    f"Пароль должен содержать минимум { min_special_chars} спецсимволов"
                )

            return func(username, password)

        return wrapper

    return decorator


def username_validator() -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(username: str, password: str) -> Any:
            if " " in username:
                raise ValueError("Имя пользователя не должно содержать пробелы")
            return func(username, password)

        return wrapper

    return decorator


@password_validator(length=10, uppercase=2, lowercase=2, special_chars=2)
@username_validator()
def register_user(username: str, password: str) -> None:
    with open("users.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(username, password)
    print(f"Пользователь {username} успешно зарегистрирован")


# Примеры использования
try:
    register_user("ИванПетров", "СуперПароль123!@")
    print("Регистрация успешна!")
except ValueError as e:
    print(f"Error: {e}")

try:
    register_user("Иван Петров", "слабый пароль")
    print("Регистрация успешна!")
except ValueError as e:
    print(f"Error: {e}")
