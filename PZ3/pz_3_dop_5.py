# Дополнительное задание 5.
# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.


def is_int(value):
  try:
    return int(value)
  except ValueError:
    return None

def check_nums() -> float:
    num1 = None
    num2 = None

    while num1 is None:
        num1 = is_int(input("Введите число 1: "))
    while num2 is None:
        num2 = is_int(input("Введите число 2: "))

    sum = num1 + num2

    if sum % 5 == 0:
       return sum + 1
    else:
       return sum -2


print(check_nums())
