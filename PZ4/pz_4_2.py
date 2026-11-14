# Дано целое число N (>0). 
# Если оно является степенью числа 3, то вывести TRUE, иначе - FALSE

def is_int(value):
    try:
        if len(value) <= 0:
            raise ValueError('Число должно быть больше 0!')
        return int(value)
    except ValueError:
        return None

def compute():
    num = None

    while num is None:
        num = is_int(input("Введите число: "))

    while num % 3 == 0:
        num //= 3
    return num == 1


print(compute())
