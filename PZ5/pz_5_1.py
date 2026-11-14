# Найдите сумму чисел ряда 1, 2, 3, 4... от числа n до чиса m. 
# Суммирование оформить функцией с параметрами. Значения n и m программа должнна зарашивать.


def is_int(value):
    try:
        return int(value)
    except ValueError:
        return None

def compute():
    num1 = None
    num2 = None

    while num1 is None:
        num1 = is_int(input("Введите число 1: "))

    while num2 is None:
        num2 = is_int(input("Введите число 2: "))
        if num2 <= num1:
            num2 = None
            print('Число должно быть больше!')

    nums = list(range(num1, num2 + 1))
    
    return sum(nums)

print(compute())
