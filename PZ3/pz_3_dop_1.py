# Дополнительное задание 1. 
# Ввести 2 числа. Если их произведение отрицательно, умножить его на 8, иначе увеличить его в 1.5 раз.


def is_float(value):
  try:
    return float(value)
  except ValueError:
    return None

def check_nums() -> float:
    num1 = None
    num2 = None

    while num1 is None:
        num1 = is_float(input("Введите число 1: "))
    while num2 is None:
        num2 = is_float(input("Введите число 2: "))

    mul = num1 * num2
    result = mul * 8 if mul < 0 else mul * 1.5

    return round(result, 1)


print(check_nums())
