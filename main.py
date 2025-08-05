import random


class Hero:
    """
    Класс, представляющий героя в игре "Битва героев".

    Атрибуты:
        name (str): Имя героя.
        health (int): Здоровье героя (по умолчанию 100).
        attack_power (int): Сила атаки героя (по умолчанию 20).
    """

    def __init__(self, name):
        self.name = name  # Имя героя
        self.health = 100  # Здоровье по умолчанию
        self.attack_power = 20  # Сила удара по умолчанию

    def attack(self, other):
        """
        Атакует другого героя(компьютер за него), нанося урон


        Args:
            other (Hero): Герой, который получает урон.
        """
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name}. у {other.name} осталось {max(0, other.health)} здоровья.")

    def is_alive(self):
        """
        Проверяет, жив ли герой (здоровье > 0)

        Returns:
            bool: True, если здоровье > 0, иначе False.
        """
        return self.health > 0


class Game:
    """
    Класс, управляющий игровым процессом.

    Атрибуты:
        player (Hero): Игрок.
        computer (Hero): Компьютерный противник.
    """

    def __init__(self, player_name):
        # Создание игроков
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

        #  Установка случайных параметров для компьютера
        self.computer.health = random.randint(80, 120)
        self.computer.attack_power = random.randint(15, 25)

    def start(self):
        """Запуск игры. Ведёт раунды до тех пор, пока оба героя живы."""
        print("=== ИГРА НАЧАЛАСЬ ===")
        print(f"Игрок: {self.player.name}, здоровье: {self.player.health}, сила атаки: {self.player.attack_power}")
        print(f"Компьютер: {self.computer.name}, здоровье: {self.computer.health}, сила атаки: {self.computer.attack_power}\n")

        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n==== Раунд {round_number} ====")
            # Ход игрока
            self.player.attack(self.computer)

            if not self.computer.is_alive():
                print(f"\n🎉  Победa! {self.player.name} одержал победу!!")
                break

            # Ход компьютера
            self.computer.attack(self.player)

            if not self.player.is_alive():
                print(f"\n💀 Проигрыш! {self.player.name} был повержен {self.computer.name}.")

            round_number += 1


if __name__ == "__main__":
    # Запуск игры
    input_name = input("Введите имя игрока: ")
    game = Game(input_name)
    game.start()

