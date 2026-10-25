# Проект Kubiki: Калькулятор квадратных уравнений 🧮

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-Free-green?style=for-the-badge)

Консольное приложение для решения квадратных уравнений с поддержкой комплексных корней, чтением/записью файлов и ведением журнала событий.

---

## 🇷🇺 Описание (Russian)

Проект Kubiki — это программа на языке Python, созданная для нахождения корней квадратного уравнения вида Ax^2 + Bx + C = 0. 

### ✨ Основные возможности:
* 📊 Вычисление корней: Программа находит как обычные (вещественные), так и комплексные корни (если дискриминант меньше нуля).
* ⌨️ Два режима ввода: Ввод коэффициентов вручную через консоль или чтение из файла data/input.txt.
* 💾 Сохранение результатов: Все ответы записываются в файл data/output.txt.
* 📝 Логирование: Все действия пользователя, введенные данные и ошибки записываются в журнал data/app.log для анализа.
* 🛑 Обработка ошибок: Защита от ввода букв вместо цифр и от деления на ноль (если A=0).
* 🧪 Автотестирование: Наличие скрипта test_kubiki.py для автоматической проверки работы модулей (библиотека unittest).

### 🚀 Установка:
1. Скачайте и установите Python 3 с официального сайта (python.org). При установке обязательно поставьте галочку "Add Python to PATH".
2. Скачайте папку с проектом (нажмите зеленую кнопку Code на GitHub и выберите Download ZIP).
3. Распакуйте архив в удобное место на компьютере.

### 📖 Как пользоваться:
1. Откройте терминал (командную строку) в папке с проектом.
2. Запустите программу командой: py src/main.py
3. В появившемся меню выберите нужное действие (введите цифру от 1 до 2 и нажмите Enter):
   - Пункт 1: Программа попросит ввести коэффициенты A, B и C с клавиатуры.
   - Пункт 2: Программа прочитает коэффициенты из файла data/input.txt (если файла нет, она создаст его с примером).
4. Результат вычислений появится на экране, сохранится в файл data/output.txt и будет записан в журнал data/app.log.

---

## 🇬🇧 Description (English)

Kubiki is a Python-based console application designed to find the roots of quadratic equations (Ax^2 + Bx + C = 0).

### ✨ Features:
* 📊 Root Calculation: Calculates both real and complex roots (when the discriminant is less than zero).
* ⌨️ Input Modes: Manual input via console or reading from data/input.txt.
* 💾 Output: Saves results to data/output.txt.
* 📝 Logging: All user actions, inputs, and errors are recorded in data/app.log for analysis.
* 🛑 Error Handling: Handles invalid inputs (letters instead of numbers) and division by zero (A=0).
* 🧪 Automated Testing: Includes test_kubiki.py for automated testing of core modules (unittest library).

### 🚀 Installation:
1. Download and install Python 3 from the official website (python.org). Make sure to check "Add Python to PATH" during installation.
2. Download the project folder (click the green Code button on GitHub and select Download ZIP).
3. Extract the archive to a convenient location on your computer.

### 📖 How to Use:
1. Open a terminal (command prompt) in the project folder.
2. Run the program with the command: py src/main.py
3. In the menu that appears, select the desired action (enter a number from 1 to 2 and press Enter):
   - Option 1: The program will ask you to enter coefficients A, B, and C from the keyboard.
   - Option 2: The program will read coefficients from data/input.txt (if the file doesn't exist, it will create one with an example).
4. The calculation result will appear on the screen, be saved to data/output.txt, and logged in data/app.log.
---

## 📁 Структура проекта (Russian)

Kubiki/

├── data/ - Файлы с данными (входные, выходные, Лог-файл app.log)

├── docs/ - Документация (ТЗ, регламент обслуживания)

├── src/ - Исходный код программы (main.py)

├── tests/ - Тест-кейсы

└── README.md - Этот файл

---

## 📁 Project Structure (English)

Kubiki/

├── data/ - Data files (input, output, app.log)

├── docs/ - Documentation (Technical requirements, maintenance)

├── src/ - Source code (main.py)

├── tests/ - Test cases

└── README.md - This file

---

Автор: Бестаева В.О <3

Created by Bestaeva V.O. <3
