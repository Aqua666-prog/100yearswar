import random
from generals import english_generals, french_generals
from events import apply_event
# === ДАННЫЕ ИГРЫ ===

# 25 исторических битв в хронологическом порядке
battles = [
    "Битва при Слёйсе (1340)", "Битва при Бланштаге (1346)", "Битва при Креси (1346)",
    "Битва при Невиллс-Кросс (1346)", "Битва при Ла-Рош-Деррьен (1347)", "Битва при Сент-Омере (1347)",
    "Битва при Пуатье (1356)", "Битва при Мелуне (1359)", "Битва при Коимбре (1360)",
    "Битва при Монтморане (1362)", "Битва при Оре (1364)", "Битва при Нахере (1367)",
    "Битва при Ла-Рошель (1372)", "Битва при Шизоре (1375)", "Битва при Отене (1379)",
    "Битва при Роузбеке (1382)", "Битва при Брив-ла-Гайарде (1387)", "Битва при Морле (1405)",
    "Битва при Азенкуре (1415)", "Битва при Вермандуа (1417)", "Битва при Пон-де-л’Арше (1418)",
    "Битва при Жаржо (1429)", "Битва при Пате (1429)", "Битва при Форминьи (1450)",
    "Битва при Кастийоне (1453)"
]

# Короли с шансом смерти 20%
kings = {
    "England": ["Эдуард III", "Ричард II", "Генрих IV", "Генрих V", "Генрих VI"],
    "France": ["Филипп VI", "Иоанн II", "Карл V", "Карл VI", "Карл VII"]
}


# Списки погибших
dead_kings = {"England": [], "France": []}
dead_generals = {"England": [], "France": []}

# Начальные армии
england_units = {"Пехота": 5, "Рыцари": 2, "Лучники": 3, "Осадные орудия": 0}
france_units = {"Пехота": 5, "Рыцари": 2, "Лучники": 3, "Осадные орудия": 0}

# Начальные короли
current_king_england = kings["England"][0]
current_king_france = kings["France"][0]

# === ГЛАВНЫЙ ЦИКЛ ИГРЫ ===
for i, battle in enumerate(battles, 1):
    apply_event()

    print(f"\n=== {i}-я битва: {battle} ===")
    print(f"👑 Король Англии: {current_king_england} | 👑 Король Франции: {current_king_france}")

    # Выбор случайного полководца
    english_general = random.choice(english_generals)
    french_general = random.choice(french_generals)


    print(f"⚔️ Полководцы: Англия — {english_general['name']} ({english_general['ability']}), "
          f"Франция — {french_general['name']} ({french_general['ability']})")

    # Определение победителя
    winner = "England" if random.random() * english_general["buff"] > random.random() * french_general["buff"] else "France"

    # Победитель получает новый юнит
    new_unit = random.choice(["Пехота", "Рыцари", "Лучники", "Осадные орудия"])
    if winner == "England":
        england_units[new_unit] += 1
    else:
        france_units[new_unit] += 1

    print(f"🏆 Победа: {winner}! Новый юнит: {new_unit}")

    # Проверка на смерть короля (20% шанс)
    if random.random() < 0.2:
        if winner == "England":
            dead_kings["France"].append(current_king_france)
            if len(kings["France"]) > 1:
                kings["France"].remove(current_king_france)
                current_king_france = kings["France"][0]
            else:
                current_king_france = "Нет короля"
            print(f"💀 Король Франции {dead_kings['France'][-1]} пал в битве! Новый король: {current_king_france}")
        else:
            dead_kings["England"].append(current_king_england)
            if len(kings["England"]) > 1:
                kings["England"].remove(current_king_england)
                current_king_england = kings["England"][0]
            else:
                current_king_england = "Нет короля"
            print(f"💀 Король Англии {dead_kings['England'][-1]} пал в битве! Новый король: {current_king_england}")

    # Проверка на смерть полководцев (10% шанс)
    if random.random() < 0.1:
        english_generals.remove(english_general)
        dead_generals["England"].append(english_general["name"])
        print(f"⚰️ Полководец Англии {english_general['name']} погиб в бою!")

    if random.random() < 0.1:
        french_generals.remove(french_general)
        dead_generals["France"].append(french_general["name"])
        print(f"⚰️ Полководец Франции {french_general['name']} погиб в бою!")

    print(f"⚔️ Армии: Англия {england_units} | Франция {france_units}")
    
    apply_event()
    
    command = input('Продолжить?: ')
    if command in ['no', 'not', 'n', "нет", "не", "ні", "н"]:
        break
# === ИТОГИ ВОЙНЫ ===
print("\n=== ИТОГИ ВОЙНЫ ===")
print(f"Погибшие короли Англии: {dead_kings['England']}")
print(f"Погибшие короли Франции: {dead_kings['France']}")
print(f"Погибшие полководцы Англии: {dead_generals['England']}")
print(f"Погибшие полководцы Франции: {dead_generals['France']}")
