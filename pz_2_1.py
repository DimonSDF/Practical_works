#Вариант 25. С начала суток прошло N секунд (N - целое). Найти кол-во полных часов, прошедших с начала суток.

def compute_hours(second: int): 
    hours = second // (60 * 60)   # 3600
    return hours

print(compute_hours(3650))
