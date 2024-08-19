#Домашняя работа

def calculate_remainder(dividend, divisor):
    """
    Функция для вычисления остатка от деления. Возвращает остаток от деления dividend на divisor.
    Если divisor равен 0, выбрасывает исключение ZeroDivisionError.
    """
    if divisor == 0:
        raise ZeroDivisionError("Деление на ноль невозможно.")
    return dividend % divisor

###################

#Урок

# def add(a, b):
#     return a + b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def multiply(a, b):
#     return a * b
#
#
# def subtract(a, b):
#     return a - b
#
#
# def mulitiply(a, b):
#     return a * b
#
#
# def divide(a, b):
#     return a - b
#
#
# def check(number):
#     return number % 2 == 0
#
# def dividezero(a, b):
#    if b == 0:
#        raise ValueError('На ноль делить нельзя')
#    return a / b