'''
Тестировать создание героев Тестировать атаку Тестировать проверку на жизнь


 Тестирование:
1 - Создания героев.
2 - Метода attack().
3 - Метода is_alive().
'''

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

    # --- ТЕСТЫ ---
if __name__ == "__main__":
        print("=== ТЕСТИРОВАНИЕ ===")

    # 1. Тест создания героев
player = Hero("Игрок")
computer = Hero("Компьютер")
print(f"Создан герой: {player.name}, здоровье: {player.health}, сила удара: {player.attack_power}")
print(f"Создан герой: {computer.name}, здоровье: {computer.health}, сила удара: {computer.attack_power}\n")

    # 2. Тест атаки
print("=== ТЕСТ АТАКИ ===")
print(f"До атаки: у {computer.name} осталось {computer.health} здоровья")
player.attack(computer)
print(f"После атаки: у {computer.name} осталось {computer.health} здоровья\n")

    # 3. Тест проверки жизни
print("=== ТЕСТ ПРОВЕРКИ ЖИЗНИ ===")
print(f"{player.name} жив? {player.is_alive()}")
print(f"{computer.name} жив? {computer.is_alive()}")

    # Уменьшим здоровье компьютера до нуля
computer.health = 0
print(f"{computer.name} жив? {computer.is_alive()}")

    # Запуск игры
print("\n=== ИГРА НАЧАЛАСЬ ===")
game = Game("Игрок")
game.start()