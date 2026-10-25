import pytest
import os
import sys
from unittest.mock import patch

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from main import solve_quadratic, get_coefficients, read_from_file, save_to_file

GREEN = '\033[92m'
RESET = '\033[0m'
tests_count = 0

def print_success(name):
    # Выводим полностью зеленую строку, как ты просила
    print(f"{GREEN}Тест {tests_count} ({name}) пройден успешно{RESET}")

def test_solve_1():
    global tests_count; tests_count += 1
    res = solve_quadratic(1, -3, 2)
    assert "x1 = 2.0" in res
    print_success("обычные корни")

def test_solve_2():
    global tests_count; tests_count += 1
    res = solve_quadratic(1, 2, 5)
    assert "j" in res
    print_success("комплексные корни")

def test_solve_3():
    global tests_count; tests_count += 1
    res = solve_quadratic(0, 5, 10)
    assert "Ошибка" in res
    print_success("нулевой A")

def test_solve_4():
    global tests_count; tests_count += 1
    res = solve_quadratic(1, 2, 1)
    assert "x1 = -1.0" in res
    print_success("один корень")

def test_solve_5():
    global tests_count; tests_count += 1
    res = solve_quadratic(1, 0, -4)
    assert "x1 = 2.0" in res
    print_success("отрицательный B")

@patch('builtins.input', side_effect=['1', '2', '3'])
def test_get_1(mock_input):
    global tests_count; tests_count += 1
    assert get_coefficients() == (1.0, 2.0, 3.0)
    print_success("ввод целых")

@patch('builtins.input', side_effect=['-1.5', '0', '10'])
def test_get_2(mock_input):
    global tests_count; tests_count += 1
    assert get_coefficients() == (-1.5, 0.0, 10.0)
    print_success("ввод дробных")

@patch('builtins.input', side_effect=['abc', '1', '2', '3'])
def test_get_3(mock_input):
    global tests_count; tests_count += 1
    assert get_coefficients() == (1.0, 2.0, 3.0)
    print_success("ввод букв")

@patch('builtins.input', side_effect=['1.1', '2.2', '3.3'])
def test_get_4(mock_input):
    global tests_count; tests_count += 1
    assert get_coefficients() == (1.1, 2.2, 3.3)
    print_success("десятичные")

@patch('builtins.input', side_effect=[' 5 ', ' 6 ', ' 7 '])
def test_get_5(mock_input):
    global tests_count; tests_count += 1
    assert get_coefficients() == (5.0, 6.0, 7.0)
    print_success("пробелы")

def test_read_1():
    global tests_count; tests_count += 1
    with open("data/test1.txt", "w") as f: f.write("1 2 3")
    coeffs, err = read_from_file("data/test1.txt")
    assert coeffs == (1.0, 2.0, 3.0) and err is None
    print_success("чтение файла")

def test_read_2():
    global tests_count; tests_count += 1
    coeffs, err = read_from_file("data/no_file.txt")
    assert "не найден" in err
    print_success("нет файла")

def test_read_3():
    global tests_count; tests_count += 1
    with open("data/test2.txt", "w") as f: f.write("1 2")
    coeffs, err = read_from_file("data/test2.txt")
    assert "3 числа" in err
    print_success("мало данных")

def test_read_4():
    global tests_count; tests_count += 1
    with open("data/test3.txt", "w") as f: f.write("a b c")
    coeffs, err = read_from_file("data/test3.txt")
    assert "нечисловые" in err
    print_success("буквы в файле")

def test_read_5():
    global tests_count; tests_count += 1
    with open("data/test4.txt", "w") as f: f.write("  1   2   3  ")
    coeffs, err = read_from_file("data/test4.txt")
    assert coeffs == (1.0, 2.0, 3.0)
    print_success("лишние пробелы")

def test_save_1():
    global tests_count; tests_count += 1
    save_to_file("data/out1.txt", "Тест")
    with open("data/out1.txt", "r", encoding="utf-8") as f: assert f.read() == "Тест"
    print_success("запись текста")

def test_save_2():
    global tests_count; tests_count += 1
    save_to_file("data/out2.txt", "")
    with open("data/out2.txt", "r", encoding="utf-8") as f: assert f.read() == ""
    print_success("пустая строка")

def test_save_3():
    global tests_count; tests_count += 1
    save_to_file("data/out3.txt", "Привет мир")
    with open("data/out3.txt", "r", encoding="utf-8") as f: assert f.read() == "Привет мир"
    print_success("кириллица")

def test_save_4():
    global tests_count; tests_count += 1
    save_to_file("data/out4.txt", "A"*1000)
    with open("data/out4.txt", "r", encoding="utf-8") as f: assert f.read() == "A"*1000
    print_success("длинный текст")

def test_save_5():
    global tests_count; tests_count += 1
    save_to_file("data/out5.txt", "Старый")
    save_to_file("data/out5.txt", "Новый")
    with open("data/out5.txt", "r", encoding="utf-8") as f: assert f.read() == "Новый"
    print_success("перезапись")

@patch('builtins.input', return_value='1')
@patch('main.get_coefficients', return_value=(1, -3, 2))
@patch('main.solve_quadratic', return_value="Успех")
@patch('main.save_to_file')
def test_main_1(mock_save, mock_solve, mock_get, mock_input):
    global tests_count; tests_count += 1
    import main
    main.main()
    mock_solve.assert_called_once_with(1, -3, 2)
    print_success("меню: ввод")

@patch('builtins.input', return_value='2')
@patch('main.read_from_file', return_value=((1, 2, 5), None))
@patch('main.solve_quadratic', return_value="Успех")
@patch('main.save_to_file')
def test_main_2(mock_save, mock_solve, mock_read, mock_input):
    global tests_count; tests_count += 1
    import main
    main.main()
    mock_read.assert_called_once()
    print_success("меню: чтение")

@patch('builtins.input', return_value='9')
def test_main_3(mock_input):
    global tests_count; tests_count += 1
    with patch('builtins.print') as mock_print:
        import main
        main.main()
        mock_print.assert_any_call("Неверный выбор.")
    print_success("меню: ошибка")

@patch('builtins.input', return_value='2')
@patch('main.read_from_file', return_value=(None, "Ошибка"))
def test_main_4(mock_read, mock_input):
    global tests_count; tests_count += 1
    with patch('builtins.print') as mock_print:
        import main
        main.main()
        mock_print.assert_any_call("Ошибка")
    print_success("меню: ошибка файла")

@patch('builtins.input', return_value='1')
@patch('main.get_coefficients', return_value=(0, 0, 0))
@patch('main.save_to_file')
def test_main_5(mock_save, mock_get, mock_input):
    global tests_count; tests_count += 1
    import main
    main.main()
    mock_save.assert_called_once()
    print_success("меню: нули")

def test_zz_final_report():
    # Просто выводим итог, без процентов и палочек
    print(f"{GREEN}Выполнено тестов: {tests_count}/25{RESET}")