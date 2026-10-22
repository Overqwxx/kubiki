import math
import cmath
import os

def solve_quadratic(a, b, c):
    """Функция для решения квадратного уравнения Ax^2 + Bx + C = 0"""
    if a == 0:
        return "Ошибка: Коэффициент A не может быть равен 0 (это не квадратное уравнение)."
    
    # Вычисляем дискриминант
    d = b**2 - 4*a*c
    
    if d >= 0:
        # Обычные (вещественные) корни
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f"Дискриминант D = {d}. Корни: x1 = {x1}, x2 = {x2}"
    else:
        # Комплексные корни (используем cmath)
        x1 = (-b + cmath.sqrt(d)) / (2*a)
        x2 = (-b - cmath.sqrt(d)) / (2*a)
        return f"Дискриминант D = {d} (меньше нуля). Комплексные корни: x1 = {x1}, x2 = {x2}"

def get_coefficients():
    """Функция для получения коэффициентов от пользователя"""
    while True:
        try:
            a = float(input("Введите коэффициент A: "))
            b = float(input("Введите коэффициент B: "))
            c = float(input("Введите коэффициент C: "))
            return a, b, c
        except ValueError:
            print("Ошибка! Пожалуйста, вводите только числа.")

def read_from_file(filename):
    """Функция для чтения коэффициентов из файла"""
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
            if len(data) < 3:
                return None, "Ошибка: в файле должно быть 3 числа (A, B, C)."
            a, b, c = float(data[0]), float(data[1]), float(data[2])
            return (a, b, c), None
    except FileNotFoundError:
        return None, f"Ошибка: файл {filename} не найден."
    except ValueError:
        return None, "Ошибка: в файле содержатся нечисловые данные."

def save_to_file(filename, text):
    """Функция для записи результата в файл"""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print(f"Результат сохранен в файл {filename}")

def main():
    print("--- Программа решения квадратных уравнений ---")
    print("1. Ввести коэффициенты вручную (консоль)")
    print("2. Прочитать коэффициенты из файла (data/input.txt)")
    
    choice = input("Выберите вариант (1 или 2): ")
    
    if choice == '1':
        a, b, c = get_coefficients()
        result = solve_quadratic(a, b, c)
        print("\n" + result)
        save_to_file("data/output.txt", result)
        
    elif choice == '2':
        # Проверяем, есть ли папка data
        if not os.path.exists("data"):
            os.makedirs("data")
            
        input_file = "data/input.txt"
        # Создадим тестовый файл, если его нет
        if not os.path.exists(input_file):
            print(f"Файл {input_file} не найден. Создаю пример...")
            with open(input_file, 'w') as f:
                f.write("1 2 5") # Пример с комплексными корнями
        
        coeffs, error = read_from_file(input_file)
        if error:
            print(error)
        else:
            a, b, c = coeffs
            print(f"Прочитаны коэффициенты: A={a}, B={b}, C={c}")
            result = solve_quadratic(a, b, c)
            print("\n" + result)
            save_to_file("data/output.txt", result)
    else:
        print("Неверный выбор.")

if __name__ == "__main__":
    main()