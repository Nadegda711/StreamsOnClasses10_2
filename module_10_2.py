import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            time.sleep(1)  # Задержка в 1 секунду
            self.enemies -= self.power
            self.days += 1
            print(f"{self.name} сражается {self.days} день(дня)..., осталось {max(self.enemies, 0)} воинов.")

        print(f"{self.name} одержал победу спустя {self.days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

second_knight.join()
first_knight.join()


print("Все битвы закончились")
