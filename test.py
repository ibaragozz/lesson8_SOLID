from abc import ABC, abstractmethod

class Health:
    def __init__(self, health: int):
        self.health = health

    def take_damage(self, damage: int):
        self.health -= damage
        print(f"Получено {damage} урона. Осталось {self.health} здоровья.")
        if self.health <= 0:
            print("Повержен!")
            return True
        return False

class Weapon(ABC):
    @abstractmethod
    def attack(self, target):
        pass

class Sword(Weapon):
    def __init__(self):
        self.damage = 15

    def attack(self, target):
        print("Атака мечом")
        if target.health.take_damage(self.damage):
            print("Монстр побежден!")

class Bow(Weapon):
    def __init__(self):
        self.damage = 10

    def attack(self, target):
        print("Стрельба из лука")
        if target.health.take_damage(self.damage):
            print("Монстр побежден!")

class Fighter():
    def __init__(self, weapon: Weapon, health: int):
        self.weapon = weapon
        self.health = Health(health)

    def change_weapon(self):
        if isinstance(self.weapon, Sword):
            self.weapon = Bow()
            print("Боец выбирает лук.")
        elif isinstance(self.weapon, Bow):
            self.weapon = Sword()
            print("Боец выбирает меч.")

    def attack(self, monster):
        if self.health.health <= 0:
            print("Боец не может атаковать, потому что он погиб (╥_╥)")
            return
        print(f"Боец атакует монстра с {type(self.weapon).__name__.lower()}.")
        self.weapon.attack(monster)

class Monster():
    def __init__(self, claw_power: int, health_monster: int):
        self.claw_power = claw_power
        self.health = Health(health_monster)  # Используем объект Health для здоровья монстра

    def attack(self, fighter: Fighter):
        if self.health.health <= 0:
            print("Монстр не может атаковать, он уже повержен!")
            return

        print("Монстр атакует бойца своими когтями.")
        if fighter.health.take_damage(self.claw_power):
            print("Боец погиб в бою!")

# Создание бойца и монстра
knight = Fighter(Sword(), 100)
himera = Monster(20, 50)

# Демонстрация боя
knight.attack(himera)  # Боец атакует с мечом

himera.attack(knight)  # Монстр атакует бойца

knight.change_weapon()  # Боец меняет оружие на лук
knight.attack(himera)  # Боец атакует с луком

himera.attack(knight)  # Монстр снова атакует бойца

knight.change_weapon()  # Боец снова меняет оружие на меч
knight.attack(himera)  # Боец атакует с мечом

himera.attack(knight)
knight.attack(himera)