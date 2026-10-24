# Дополнительное задание 2. 
# Ввести число. Если оно чётное, разделить его на 4, если нечётное, умножить на 5.


def is_float(value):
  try:
    return float(value)
  except ValueError:
    return None

def check_num() -> float:
    num = None

    while num is None:
        num = is_float(input("Введите число: "))

    result = (num / 4) if (num % 2 == 0) else (num * 5)

    return round(result, 1)


print(check_num())
