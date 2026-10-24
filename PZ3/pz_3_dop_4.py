# Дополнительное задание 4.
# Дано целое число. Если оно является положительным, прибавить 20, иначе вычесть 5. 


def is_int(value):
  try:
    return int(value)
  except ValueError:
    return None

def check_num() -> int:
    num = None

    while num is None:
        num = is_int(input("Введите число: "))

    if num > 0:
        return num + 20
    else:
       return num - 5


print(check_num())
