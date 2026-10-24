import math
import cmath
import os
import logging

# Настройка логирования (запись событий в файл data/app.log)
logging.basicConfig(
    filename='data/app.log', 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def solve_quadratic(a, b, c):
    logging.info(f"Запуск решения уравнения: A={a}, B={b}, C={c}")
    if a == 0:
        logging.error("Ошибка: Коэффициент A равен 0.")
        return "Ошибка: Коэффициент A не может быть равен 0 (это не квадратное уравнение)."
    
    d = b**2 - 4*a*c
    logging.info(f"Вычислен дискриминант: D={d}")
    
    if d >= 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        logging.info(f"Найдены вещественные корни: x1={x1}, x2={x2}")
        return f"Дискриминант D = {d}. Корни: x1 = {x1}, x2 = {x2}"
    else:
        x1 = (-b + cmath.sqrt(d)) / (2*a)
        x2 = (-b - cmath.sqrt(d)) / (2*a)
        logging.info(f"Найдены комплексные корни: x1={x1}, x2={x2}")
        return f"Дискриминант D = {d} (меньше нуля). Комплексные корни: x1 = {x1}, x2 = {x2}"

def get_coefficients():
    while True:
        try:
            a = float(input("Введите коэффициент A: "))
            b = float(input("Введите коэффициент B: "))
            c = float(input("Введите коэффициент C: "))
            logging.info(f"Пользователь ввел коэффициенты: {a}, {b}, {c}")
            return a, b, c
        except ValueError:
            logging.warning("Ошибка ввода: введено не число.")
            print("Ошибка! Пожалуйста, вводите только числа.")

def read_from_file(filename):
    logging.info(f"Попытка чтения данных из файла: {filename}")
    try:
        with open(filename, 'r') as file:
            data = file.read().split()
            if len(data) < 3:
                logging.error(f"В файле {filename} недостаточно данных.")
                return None, "Ошибка: в файле должно быть 3 числа (A, B, C)."
            a, b, c = float(data[0]), float(data[1]), float(data[2])
            logging.info(f"Данные успешно прочитаны: A={a}, B={b}, C={c}")
            return (a, b, c), None
    except FileNotFoundError:
        logging.error(f"Файл {filename} не найден.")
        return None, f"Ошибка: файл {filename} не найден."
    except ValueError:
        logging.error(f"В файле {filename} содержатся нечисловые данные.")
        return None, "Ошибка: в файле содержатся нечисловые данные."

def save_to_file(filename, text):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Результат сохранен в {filename}")
        logging.info(f"Результат успешно сохранен в файл: {filename}")
    except Exception as e:
        logging.error(f"Ошибка при сохранении в файл {filename}: {e}")
        print(f"Не удалось сохранить результат: {e}")

def main():
    # Проверяем, существует ли папка data. Если нет - создаем.
    if not os.path.exists("data"):
        os.makedirs("data")

    logging.info("--- Запуск программы ---")
    print("--- Программа решения квадратных уравнений ---")
    print("1. Ввести коэффициенты вручную")
    print("2. Прочитать из файла")
    
    choice = input("Выберите вариант (1 или 2): ")
    logging.info(f"Пользователь выбрал пункт меню: {choice}")
    
    if choice == '1':
        a, b, c = get_coefficients()
        result = solve_quadratic(a, b, c)
        print("\n" + result)
        save_to_file("data/output.txt", result)
        
    elif choice == '2':
        input_file = "data/input.txt"
        if not os.path.exists(input_file):
            print(f"Файл {input_file} не найден. Создаю пример...")
            logging.warning(f"Файл {input_file} не найден. Создан файл с примером.")
            with open(input_file, 'w') as f:
                f.write("1 2 5") 
        
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
        logging.warning(f"Пользователь ввел неверный пункт меню: {choice}")

if __name__ == "__main__":
    main()