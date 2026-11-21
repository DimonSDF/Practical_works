# Описать функцию DigitCountSum(K, C, S), находящую количество C цифр целого
# положительного числа K, а также их сумму S (K — входной, C и S — выходные
# параметры целого типа). С помощью этой функции найти количество и сумму цифр
# для каждого из пяти данных целых чисел.


def DigitCountSum(K: int):
    num = str(K)
    C = len(num)
    S = sum(map(int, num))
    return C, S

def is_int(value):
    try:
        num = int(value)
        if num < 0:
            raise ValueError('Число должно быть больше 0!')
        return num
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

def check_foo():
    num = None

    while num is None:
        num = is_int(input("Введите число: "))

    print(DigitCountSum(num))


