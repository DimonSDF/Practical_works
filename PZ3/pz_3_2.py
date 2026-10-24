# Вариант 25. Даны координаты поля шахматной доски (x, y). 
# Учитывая, что поле (1, 1) является чёрным, проверить истинность высказывания "Данное поле является белым".


def is_coord(value):
    try:
        num = int(value)
        if num < 1 or num > 8:
            raise ValueError("Координаты поля находятся в диапозоне от 1 до 8.")
        return num
    except ValueError as e:
        print(f"Ошибка: {e}")
        return None

def check_coord():
    x = None
    y = None

    while x is None:
        x = is_coord(input("Введите координату (x): "))
    while y is None:
        y = is_coord(input("Введите координату (y): "))

    if (x + y) % 2 == 0:
        return False
    else:
        return True

print(check_coord())
