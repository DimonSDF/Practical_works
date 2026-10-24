# Вариант 25. Даны числа x, y. 
# Проверить истинность высказывания "Точка с координатами (x, y) лежит во второй координатной четверти."


def is_float(value):
  try:
    return float(value)
  except ValueError:
    return None

def check_coord() -> bool:
  x = None
  y = None

  while x is None:
    x = is_float(input("Введите абсциссу (x): "))
  while y is None:
    y = is_float(input("Введите ординату (y): "))

  return x < 0 and y > 0


print(check_coord())
