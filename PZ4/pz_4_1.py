# Даны два целых числа A и B (A < B). 
# Вывести в порядке возрастания все цилые числа, расположенные между A и B (включая сами числа A и B), а также количество N этих чисел


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

    return(nums, len(nums))

print(compute())

    
