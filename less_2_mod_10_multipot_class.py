# -*- coding: utf-8 -*-
import time
from threading import Thread

class Knight(Thread):
    """Счетчик сражения"""
    def __init__(self, name, scill):
        Thread.__init__(self)
        self.name = name
        self.scill = scill
    def run(self):
        print(f"{self.name} на нас напали!")
        enamy = 100
        days = enamy / self.scill
        days = int(days)
        for day in range(1, days+1):
            enamy = enamy - self.scill
            print(f"{self.name} сражается {day} день(дня)..., осталось {enamy} войнов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {days} дней!")


knight1 = Knight(name="Sir Lancelot", scill=10)  # Низкий уровень умения
knight2 = Knight(name="Sir Galahad", scill=20)  # Высокий уровень умения
knight1.start()
knight2.start()
knight1.join()
knight2.join()
print("Всё! Битва закончилась!")
