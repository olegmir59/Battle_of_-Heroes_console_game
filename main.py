class Hero:
    def __init__(self, name):
        self.name = name  # Имя героя
        self.health = 100  # Здоровье по умолчанию
        self.attack_power = 20  # Сила удара по умолчанию

    def attack(self, other):
        """Атакует другого героя(компьютер за него), нанося урон"""
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name}. У {other.name} осталось {other.health} здоровья.")

    def is_alive(self):
        """Проверяет, жив ли герой (здоровье > 0)"""
        return self.health > 0
