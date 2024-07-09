# -*- coding: utf-8 -*-
import threading
from threading import Thread
import time
import queue


class Table:

    def __init__(self, number=int, is_busy=bool):

        self.number = number
        self.is_busy = is_busy
        super().__init__()


    def run(self):
        if self.is_busy == True:
            print(f"Свободен  {self.number} столик.")
        else:
            print(f"Занят  {self.number} столик.")


class Cafe:
    """"""
    def __init__(self, tables):
        self.q = queue.Queue(maxsize=3)
        self.tables = tables
        super().__init__()


    def customer_arrival(self):
        """моделирует приход посетителя(каждую секунду)"""
        self.customer = 0
        while self.customer < 20:
            self.customer += 1
            print(f"Посетитель {self.customer} прибыл.")
            self.serv_customer(self.customer)
            time.sleep(1)


    def serv_customer(self, customer):
        """моделирует обслуживание посетителя.
        Проверяет наличие свободных столов, в случае наличия стола -
         начинает обслуживание посетителя (запуск потока),
         в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд."""

        self.q.put(customer)
        for i in range(len(tables)):
            tt = tables[i].is_busy
            if tt == True:
                while not self.q.empty():
                    Customer(i + 1, self.q.get()).start()


class Customer(Thread):
    """Запускается, если есть свободные столы."""
    def __init__(self, table, customer):
        super().__init__()
        self.customer = customer
        self.table = table

    def run(self):
        print(self.table)
        print(f"Посетитель номер {self.customer} сел за стол {self.table}.")
        tables[self.table - 1].is_busy = False
        if tables[self.table - 1].is_busy == False:
            print(f"Столик {self.table} занят")
        time.sleep(5)
        print(f"Посетитель номер {self.customer} покушал и ушёл.")
        tables[self.table - 1].is_busy = True


# Создаем столики в кафе

table1 = Table(1, is_busy=True)
table2 = Table(2, is_busy=True)
table3 = Table(3, is_busy=True)
tables = [table1, table2, table3]
# Инициализируем кафе
cafe = Cafe(tables)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

