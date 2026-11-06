import os

# Имя файла для логирования ошибок ввода
LOG_FILENAME = "input_errors.log"

def log_error(message: str) -> None:
    """Записывает ошибку в лог-файл."""
    try:
        with open(LOG_FILENAME, "a", encoding="utf-8") as f:
            f.write(f"{message}\n")
    except Exception:
        pass

def input_number(prompt: str) -> float:
    """Запрашивает у пользователя число с защитой от некорректного ввода (без break)."""
    is_valid = False
    value = 0.0
    
    while not is_valid:
        raw = input(prompt).strip()
        try:
            value = float(raw)
            is_valid = True
        except ValueError:
            msg = f"Ошибка: введено не число ('{raw}')."
            print(msg)
            log_error(msg)
            print("Повторите ввод.")

    return value

def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    """Проверяет попадание значения в диапазон [low, high]."""
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    if value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    return True, ""

def get_validated_range_value(low: float, high: float, prompt_desc: str) -> float:
    """Запрашивает число и проверяет его нахождение в диапазоне (без использования break)."""
    valid = False
    result_value = 0.0

    while not valid:
        raw_val = input_number(f"Введите {prompt_desc} в диапазоне [{low}, {high}]: ")
        ok, msg = validate_range(raw_val, low, high)
        if ok:
            result_value = raw_val
            valid = True
        else:
            print(msg + " Повторите ввод.")
            log_error(msg)

    return result_value

def calculate_linear_function(x: float, a: float, b: float) -> float:
    """Пример расчетной функции: y = a * x + b"""
    return a * x + b

def main_menu():
    """Главное меню программы."""
    running = True
    
    while running:
        print("\n=== ЛАБОРАТОРНАЯ РАБОТА (Вариант 9) ===")
        print("1. Выполнить расчет по формуле")
        print("2. Просмотреть лог ошибок ввода")
        print("3. Выход")
        
        choice_str = input("Выберите пункт меню (1-3): ").strip()
        
        if choice_str == '1':
            print("\n--- Введите параметры для расчета ---")
            a = input_number("Введите коэффициент a: ")
            b = input_number("Введите коэффициент b: ")
            x = get_validated_range_value(-100.0, 100.0, "значение x (-100...100)")
            
            result = calculate_linear_function(x, a, b)
            print(f"\nРезультат расчета y = {a} * {x} + {b} равен: {result}")
            
        elif choice_str == '2':
            print("\n--- Содержимое файла логов ---")
            if os.path.exists(LOG_FILENAME):
                with open(LOG_FILENAME, "r", encoding="utf-8") as f:
                    content = f.read()
                    if content:
                        print(content)
                    else:
                        print("Лог-файл пуст.")
            else:
                print("Лог-файла пока нет (ошибок ввода еще не было).")
                
        elif choice_str == '3':
            print("Завершение работы программы. Удачи на сдаче!")
            running = False
        else:
            print("Неверный выбор. Пожалуйста, введите число от 1 до 3.")

if __name__ == "__main__":
    main_menu()
