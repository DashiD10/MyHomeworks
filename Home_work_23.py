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