# Проект Kubiki: Калькулятор квадратных уравнений 🧮

![Python](https://img.shields.io/badge/Python-3.6+-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-Free-green?style=for-the-badge)

*Консольное приложение для решения квадратных уравнений с поддержкой комплексных корней, чтением/записью файлов и созданием резервных копий.*

---

## 🇷🇺 Описание (Russian)

Проект Kubiki — это программа на языке Python, созданная для нахождения корней квадратного уравнения вида Ax^2 + Bx + C = 0. 

### ✨ Основные возможности:
*   📊 Вычисление корней: Программа находит как обычные (вещественные), так и комплексные корни (если дискриминант меньше нуля).
*   ⌨️ Два режима ввода: Ввод коэффициентов вручную через консоль или чтение из файла data/input.txt.
*   💾 Сохранение результатов: Все ответы записываются в файл data/output.txt.
*   🛡️ Резервное копирование: Возможность сделать бэкап введенных коэффициентов и восстановить их при необходимости.
*   🛑 Обработка ошибок: Защита от ввода букв вместо цифр и от деления на ноль (если A=0).

### 🚀 Как запустить:
1. Убедитесь, что у вас установлен Python 3.
2. Откройте терминал в папке с проектом.
3. Запустите программу командой:
   py src/main.py

---

## 🇬🇧 Description (English)

Kubiki is a Python-based console application designed to find the roots of quadratic equations (Ax^2 + Bx + C = 0).

### ✨ Features:
*   📊 Root Calculation: Calculates both real and complex roots (when the discriminant is less than zero).
*   ⌨️ Input Modes: Manual input via console or reading from data/input.txt.
*   💾 Output: Saves results to data/output.txt.
*   🛡️ Backup System: Create and restore backups of input coefficients.
*   🛑 Error Handling: Handles invalid inputs (letters instead of numbers) and division by zero (A=0).

### 🚀 How to Run:
1. Make sure Python 3 is installed.
2. Open a terminal in the project folder.
3. Run the program with the command:
   py src/main.py

---

## 📁 Структура проекта / Project Structure

Kubiki/
├── data/               # Файлы с данными (входные, выходные, бэкапы)
├── docs/               # Документация (ТЗ, регламент обслуживания)
├── src/                # Исходный код программы (main.py)
├── tests/              # Тест-кейсы
└── README.md           # Этот файл

---
![Jokes Card](https://readme-jokes.vercel.app/api?theme=dark)ц