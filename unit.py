import random

# === Базовый класс юнита ===
class Unit:
    def __init__(self, name, health, damage, accuracy, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.accuracy = accuracy
        self.armor = armor

    def attack(self, enemy):
        """Юнит атакует врага один раз."""
        if random.randint(1, 100) <= self.accuracy:
            actual_damage = max(0, self.damage - enemy.armor)
            enemy.health -= actual_damage
            return actual_damage
        return 0

    def is_alive(self):
        return self.health > 0

    def __repr__(self):
        return f"{self.name} (❤️ {self.health}, ⚔️ {self.damage}, 🎯 {self.accuracy}%, 🛡️ {self.armor})"

# === Юниты Англии ===

class EnglishBillman(Unit):
    """Английский копейщик с боевой косой (бил)."""
    def __init__(self):
        super().__init__("Английский билмен", health=100, damage=30, accuracy=70, armor=15)

class EnglishLongbowman(Unit):
    """Английский лучник с длинным луком."""
    def __init__(self):
        super().__init__("Английский лучник", health=80, damage=35, accuracy=85, armor=5)

class EnglishKnight(Unit):
    """Тяжелая кавалерия Англии."""
    def __init__(self):
        super().__init__("Английский рыцарь", health=150, damage=50, accuracy=75, armor=30)

class EnglishBombard(Unit):
    """Английская бомбарда — мощная, но медленная пушка."""
    def __init__(self):
        super().__init__("Английская бомбарда", health=200, damage=120, accuracy=50, armor=5)

# === Юниты Франции ===

class FrenchPikeman(Unit):
    """Французский пикинёр, силен против кавалерии."""
    def __init__(self):
        super().__init__("Французский пикинёр", health=110, damage=35, accuracy=65, armor=20)

class FrenchCrossbowman(Unit):
    """Генуэзский арбалетчик на французской службе."""
    def __init__(self):
        super().__init__("Французский арбалетчик", health=85, damage=40, accuracy=80, armor=10)

class FrenchKnight(Unit):
    """Французский рыцарь — мощная кавалерия."""
    def __init__(self):
        super().__init__("Французский рыцарь", health=160, damage=55, accuracy=70, armor=35)

class FrenchTrebuchet(Unit):
    """Французский требушет — осадное орудие."""
    def __init__(self):
        super().__init__("Французский требушет", health=220, damage=100, accuracy=55, armor=5)

# === Функция битвы ===

def battle(unit1, unit2):
    """Один раунд боя между двумя юнитами (по одному удару)."""
    print(f"⚔️ Бой: {unit1.name} vs {unit2.name} ⚔️")
    counter = 0
    while(True):
        counter += 1
        
        damage1 = unit1.attack(unit2)
        damage2 = unit2.attack(unit1)

        print(f"{unit1.name} наносит {damage1} урона! (❤️ {unit2.health})")
        print(f"{unit2.name} наносит {damage2} урона! (❤️ {unit1.health})")
        
        if unit1.is_alive() and not unit2.is_alive():
            print(f"🏆 Победил {unit1.name}!")
        elif unit2.is_alive() and not unit1.is_alive():
            print(f"🏆 Победил {unit2.name}!")
        elif not unit1.is_alive() and not unit2.is_alive():
            print("💀 Оба юнита погибли!")
        else:
            print("⚔️ Битва продолжается...")

        print("-" * 40)
        
        if counter==1000: 
            print('Битва шла больше тысячи циклов')
            break
        
        if not unit1.is_alive() or not unit2.is_alive():
            print(f'Битва шла {counter} циклов')
            break

        
# === Симуляция битв ===

if __name__ == "__main__":
    eng_billman = EnglishBillman()
    fr_pikeman = FrenchPikeman()

    eng_longbow = EnglishLongbowman()
    fr_crossbow = FrenchCrossbowman()

    eng_knight = EnglishKnight()
    fr_knight = FrenchKnight()

    eng_bombard = EnglishBombard()
    fr_trebuchet = FrenchTrebuchet()

    # Проведение боёв
    battle(eng_billman, fr_pikeman)  # Копейщики
    battle(eng_longbow, fr_crossbow)  # Лучники
    battle(eng_knight, fr_knight)  # Рыцари
    battle(eng_bombard, fr_trebuchet)  # Артиллерия