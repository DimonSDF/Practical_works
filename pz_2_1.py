#Вариант 25. С начала суток прошло N секунд (N - целое). Найти кол-во полных часов, прошедших с начала суток.

def compute_hours(second: int) -> int: 
    hours = second // (60 * 60)   # 3600
    return hours

while True:
    try:
        sec = int(input("Введите кол-во секунд: "))
        
        if sec < 0:
            raise ValueError("Кол-во секунд не может быть отрицательным")
        elif sec > 86400:
            raise ValueError("Кол-во секунд не может быть больше, чем есть в сутках")
            
    except ValueError as e:
        print(f"Ошибка ввода: {e}. Попробуйте ещё раз.")
        
    hours = compute_hours(sec)
    print(f"Прошло полных часов: {hours}.")
    break
