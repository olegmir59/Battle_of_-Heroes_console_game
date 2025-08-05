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
        self.name = name
        self.health = 100
        self.attack_power = 20

    def attack(self, other):
        """
        Атакует другого героя, нанося урон.

        Args:
            other (Hero): Герой, который получает урон.
        """
        other.health -= self.attack_power
        print(f"{self.name} атаковал {other.name}. У {other.name} осталось {max(0, other.health)} здоровья.")

    def is_alive(self):
        """
        Проверяет, жив ли герой.

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

        # Установка случайных параметров для компьютера
        self.computer.health = random.randint(80, 120)
        self.computer.attack_power = random.randint(15, 25)

    def start(self):
        """Запуск игры. Ведёт раунды до тех пор, пока оба героя живы."""
        print("=== ИГРА НАЧАЛАСЬ ===")
        print(f"Игрок: {self.player.name}, здоровье: {self.player.health}, сила атаки: {self.player.attack_power}")
        print(
            f"Компьютер: {self.computer.name}, здоровье: {self.computer.health}, сила атаки: {self.computer.attack_power}\n")

        round_number = 1

        while self.player.is_alive() and self.computer.is_alive():
            print(f"\n==== Раунд {round_number} ====")
            # Ход игрока
            self.player.attack(self.computer)

            if not self.computer.is_alive():
                print(f"\n🎉 Победа! {self.player.name} одержал победу над {self.computer.name}!")
                break

            # Ход компьютера
            self.computer.attack(self.player)

            if not self.player.is_alive():
                print(f"\n💀 Проигрыш! {self.player.name} был повержен {self.computer.name}.")

            round_number += 1


def run_tests():
    """Тестирует различные сценарии игры."""
    print("=== ТЕСТИРОВАНИЕ РАЗЛИЧНЫХ СЦЕНАРИЕВ ===\n")

    # Сценарий 1: Игрок выигрывает на первом ходу
    print("Сценарий 1: Игрок выигрывает на первом ходу")
    player = Hero("Игрок")
    computer = Hero("Компьютер")
    computer.health = 10  # Минимальное здоровье, чтобы игрок мог победить за один удар
    print(f"До атаки: {computer.health} здоровья")
    player.attack(computer)
    assert not computer.is_alive()
    print("✅ Тест пройден\n")

    # Сценарий 2: Компьютер выигрывает на первом ходу
    print("Сценарий 2: Компьютер выигрывает на первом ходу")
    player = Hero("Игрок")
    player.health = 10  # Минимальное здоровье, чтобы компьютер мог победить за один удар
    computer = Hero("Компьютер")
    computer.attack(player)
    assert not player.is_alive()
    print("✅ Тест пройден\n")

    # Сценарий 3: Игра длится несколько раундов
    print("Сценарий 3: Игра длится несколько раундов")
    player = Hero("Игрок")
    computer = Hero("Компьютер")
    player.health = 60
    computer.health = 60
    rounds = 0
    while player.is_alive() and computer.is_alive():
        player.attack(computer)
        if not computer.is_alive():
            break
        computer.attack(player)
        rounds += 1
    assert rounds >= 2
    print(f"Игра продолжалась {rounds + 1} раундов. ✅ Тест пройден\n")

    # Сценарий 4: Герой получает нулевое здоровье
    print("Сценарий 4: Герой получает нулевое здоровье")
    hero = Hero("Герой")
    hero.health = 20
    enemy = Hero("Противник")
    enemy.attack_power = 20
    enemy.attack(hero)
    assert hero.health == 0
    assert not hero.is_alive()
    print("✅ Тест пройден\n")

    # Сценарий 5: У героя сила атаки равна 0
    print("Сценарий 5: У героя сила атаки равна 0")
    hero = Hero("Герой")
    hero.attack_power = 0
    enemy = Hero("Противник")
    hero.attack(enemy)
    assert enemy.health == 100
    print("✅ Тест пройден\n")


if __name__ == "__main__":
    run_tests()
