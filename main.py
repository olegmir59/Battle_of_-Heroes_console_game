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


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Игра началась!")
        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\nРаунд {round_number}")
            # Ход игрока
            self.player.attack(self.computer)

            if not self.computer.is_alive():
                print(f"{self.computer.name} погиб. Победил {self.player.name}!")
                break

            # Ход компьютера
            self.computer.attack(self.player)

            if not self.player.is_alive():
                print(f"{self.player.name} погиб. Победил {self.computer.name}!")

            round_number += 1
