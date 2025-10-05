# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    n = n % 86400
    hours = n // 3600
    n %= 3600
    minutes = n // 60
    seconds = n % 60
    print(f"{hours}:{minutes:02d}:{seconds:02d}")

   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()