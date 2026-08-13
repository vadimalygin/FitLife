# Проект FitLife - MVP версия 1.0

# Константы для перевода единиц измерения
MLITER_PER_LITER = 1000
WATER_PER_KG = 30

# Определение функций для сбора данных о возрасте, весе и росте


def get_age() -> tuple[int, bool]:
    """Сбор данных о возрасте пользователя с флагом"""
    try:
        user_age = int(input("Введите ваш возраст: "))
        has_no_age = False
        return user_age, has_no_age
    except Exception:
        print("Некорректный формат ввода. Попробуйте ещё раз.")
        raise


def get_weight() -> tuple[float, bool]:
    """Сбор данных о весе пользователя с флагом"""
    try:
        user_weight = float(input("Введите ваш вес (в кг): "))
        has_no_weight = False
        return user_weight, has_no_weight
    except Exception:
        print("Некорректный формат ввода. Попробуйте ещё раз.")
        raise


def get_height() -> tuple[float, bool]:
    """Сбор данных о росте пользователя с флагом"""
    try:
        user_height = float(input("Введите ваш рост в м.(например 1.75): "))
        has_no_height = False
        return user_height, has_no_height
    except Exception:
        print("Некорректный формат ввода. Попробуйте ещё раз.")
        raise


# Сбор данных пользователя
user_name = input("\nДобрый день! Как к вам обращаться?: ").title()

# Дожидаемся пока пользователь введёт все данные корректно
has_no_age = True
has_no_weight = True
has_no_height = True

while has_no_age or has_no_weight or has_no_height:
    try:
        if has_no_age:
            user_age, has_no_age = get_age()

        if has_no_weight:
            user_weight, has_no_weight = get_weight()

        if has_no_height:
            user_height, has_no_height = get_height()
    except Exception:
        continue

# Расчёт рекомендованных значений
bmi = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / MLITER_PER_LITER

# Определение необходимого слова для числа возраста (год[а]/лет)
is_one_to_four = user_age % 10 in [1, 2, 3, 4]
is_exception = user_age % 100 in [11, 12, 13, 14]

age_ending = 'г' if (is_one_to_four and not is_exception) else 'л'

# Вывод отчёта о пользователе
print('\n', '-' * 42, sep='')
print(f"Отчёт для пользователя: {user_name} ({user_age} {age_ending}.)")
print(f"Индекс массы тела (ИМТ): {bmi:.1f}")
print(f"Норма воды (в литрах): {water_l:.1f} в день")
print('-' * 42)
print("\nРасчёт окончен. Будьте здоровы!")
