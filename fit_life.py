# Проект FitLife - MVP версия 1.0

# Константы для перевода единиц измерения
MLITER_PER_LITER = 1000 
WATER_PER_KG = 30 

# Сбор данных пользователя
user_name = input("\nДобрый день! Как к вам обращаться?: ").title()

# Дожидаемся пока пользователь введёт все данные корректно
has_no_age = True
has_no_weight = True
has_no_height = True

while has_no_age or has_no_weight or has_no_height:
    if has_no_age:
        try:
            user_age = int(input("Введите ваш возраст: "))
            has_no_age = False
        except Exception as e:
            print("Некорректный формат ввода. Попробуйте ещё раз.")
            continue

    if has_no_weight:
        try:
            user_weight = float(input("Введите ваш вес (в кг): "))
            has_no_weight = False
        except Exception as e:
            print("Некорректный формат ввода. Попробуйте ещё раз.")
            continue


    if has_no_height:
        try:
            user_heiht = float(input("Введите ваш рост в м. (например 1.75): "))
            has_no_height = False
        except Exception as e:
            print("Некорректный формат ввода. Попробуйте ещё раз.")
            continue

# Расчёт рекомендованных значений
bmi = round(user_weight / (user_heiht ** 2), 1)
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
