import random
import string

# Генерация случайного email
def generate_email():
    """Генерация уникального email"""
    return f"{generate_string(10)}@example.com"

# Генерация пароля
def generate_password(length=8):
    """Генерация пароля заданной длины"""
    return generate_string(length)

# Функция для генерации случайной строки
def generate_string(length):
    """Генерация случайной строки из букв и цифр"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))