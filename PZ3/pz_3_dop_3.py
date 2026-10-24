# Дополнительное задание 3. 
# Ввести двузначное число. Если сумма цифр чётная, увеличить его на 2, если нечётная, уменьшить на 2.


def is_int(value):
  try:
    if len(value) != 2:
       raise ValueError
    return int(value)
  except ValueError:
    return None

def check_num() -> int:
    num = None

    while num is None:
        num = is_int(input("Введите число: "))


    if sum(map(int, str(num))) % 2 == 0:
        return num + 2
    else:
       return num - 2


print(check_num())
