# спрашиваем имя

WATER_PER_KG = 30
STEPS_PER_YEAR = 100

# Цикл имя
while True:
    user_name = input("Введите ваше имя: ").strip()
    if len(user_name) > 0:
        break
    else:
        print("Вы не ввели свое имя!")
# Цикл спрашиваем возраст
while True:
    try:
        user_age = int(input("Какой у вас возраст? "))
        if user_age > 0:
            break
        else:
            print("Возраст не может быть меньше нуля!")
    except ValueError:
        print("Введите возраст только цифрами!")
# Цикл спрашиваем вес в кг
while True:
    try:
        mass = float(input("Какой у вас вес (например 83.5): "))
        if mass > 0:
            break
        else:
            print("Вес не может быть отрицательным")
    except ValueError:
        print("Вес указывают только цифрами!")
# спрашиваем рост
while True:
    try:
        user_high = float(input("Введите ваш рост через точку: "))
        if user_high > 0:
            break
        else:
            print("Рост не может быть отрицательным")
    except ValueError:
        print("Укажите рост только цифрами!")


# Выводим функцию для рассчета ИМТ
def imt_user():
    imt = mass / user_high ** 2
    if imt < 18.5:
        print("Недостаточный вес")
    elif 25 < imt < 29.9:
        print('Избыточный вес')
    elif 18.5 < imt < 24.9:
        print('Норма')
    else:
        imt > 30
        print('Ожирение')


# Норма воды
water = float(mass * WATER_PER_KG / 1000)
# Норма шагов
steps_user = user_age * 100
# Норма сна
user_sleep = 8 * (user_age // 30) * 0.5

# Отчет для пользователя: Иван, (25 г.)
# ИМТ: 23.4 — Норма
# Рекомендуемая норма воды: 2.55 л. в день
# Рекомендуемая норма шагов: 2500 шагов
# Рекомендуемая норма сна: 8.0 ч.

# Выводим красивый текст
print(f"Привет {user_name} !")
print(f"Тебе {user_age} лет")
print(f"Ваш вес: {mass}")
print(f"Ваш рост: {user_high}")
imt_user()
