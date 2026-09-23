# спрашиваем имя

WATER_PER_KG_W = 30
WATER_PER_KG_M = 35
STEPS_PER_YEAR = 100

# Цикл имя
while True:
    user_name = input("Здравствуйте, введите ваше имя: ").strip()
    if len(user_name) > 0:
        break
    else:
        print("Вы не ввели свое имя!")
# Цикл спрашиваем возраст
while True:
    try:
        user_age = int(input("Укажите ваш возраст: "))
        if user_age > 0:
            break
        else:
            print("Возраст не может быть меньше нуля!")
    except ValueError:
        print("Введите возраст только цифрами!")
# Цикл спрашиваем вес в кг
while True:
    try:
        mass = float(input("Укажите ваш вес(например 83.5): "))
        if mass > 0:
            break
        else:
            print("Вес не может быть отрицательным")
    except ValueError:
        print("Вес указывают только цифрами!")
# спрашиваем рост
while True:
    try:
        user_high = float(input("Укажите ваш рост в метрах(например 1.81): "))
        if 0 < user_high <= 0.5:
            print('Рост не может быть меньше 50см')
        elif user_high >= 2.5:
            print('Не бывает таких высоких людей!')
        elif user_high < 0:
            print('Рост не может быть отрицательным')
        else:
            break
    except ValueError:
        print("Укажите рост только цифрами!")
# Спрашиваем пол
user_sex = int(input('Укажите ваш пол (1 - мужчина, 2 - женщина): '))
if user_sex == 1:
    # Считаем норму воды
    water = float(mass * WATER_PER_KG_M / 1000)
else:
    water = float(mass * WATER_PER_KG_W / 1000)
# Выводим ИМТ
imt = mass / user_high ** 2
imt = round(imt, 1)
if imt <= 18.5:
    a = "Недостаточный вес"
elif 25 < imt < 29.9:
    a = 'Избыточный вес'
elif 18.5 < imt < 24.9:
    a = 'Норма'
else:
    a = 'Ожирение'


# Норма шагов
steps_user = user_age * 100
# Норма сна
user_sleep = 8 - (user_age/30)*0.5
# Выводим красивый текст
print(f"Отчет для пользователя: {user_name}, ({user_age}г.)")
print(f"ИМТ: {imt} — {a}")
print(f"Рекомендуемая норма воды: {water} л. в день")
print(f"Рекомендуемая норма шагов: {steps_user} в день")
print(f"Рекомендуемая норма сна: {user_sleep} ч.")
print('Расчет окончен. Будьте здоровым!')
