# Проект FitLife - MVP версия 1.0

WATER_PER_KG = 30

# Сбор данных пользователя
user_name = input("\nДобрый день! Как к вам обращаться?: ").title()
user_age = int(input("Введите ваш возраст: "))
user_weight = float(input("Введите ваш вес (в кг): "))
user_heiht = float(input("Введите ваш рост (в метрах) (например 1.75): "))

# Расчёт рекомендованных значений
bmi = round(user_weight / (user_heiht ** 2), 1)
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / 1000

# Определение необходимого слова для числа возраста (год[а]/лет)
age_ending = 'г' if (user_age % 10 in [1, 2, 3, 4]
                     and user_age % 100 not in [11, 12, 13, 14]) else 'л'

# Вывод отчёта о пользователе
print('\n', '-' * 42, sep='')
print(f"Отчёт для пользователя: {user_name} ({user_age} {age_ending}.)")
print(f"Индекс массы тела (ИМТ): {bmi:.1f}")
print(f"Норма воды (в литрах): {water_l:.1f} в день")
print('-' * 42)
print("\nРасчёт окончен. Будьте здоровы!")
