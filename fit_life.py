# Проект FitLife - MVP версия 1.0

MLITER_PER_LITER = 1000 # Не сочтите за грубость но помоему это очевидно
WATER_PER_KG = 30

# Сбор данных пользователя
user_name = input("\nДобрый день! Как к вам обращаться?: ").title()
user_age = int(input("Введите ваш возраст: "))
user_weight = float(input("Введите ваш вес (в кг): "))
user_heiht = float(input("Введите ваш рост (в метрах) (например 1.75): "))

# Расчёт рекомендованных значений
bmi = round(user_weight / (user_heiht ** 2), 1)
water_ml = user_weight * WATER_PER_KG # Зачем нужна эта переменная? Или она не занимает место в памяти? т.к. ссылка на экз класса инт?
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
