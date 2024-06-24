#!/usr/bin/python3
# -*- coding: utf-8 -*-
from threading import Thread, Lock

class BankAccount:
    """Добавление в депозитб снятие с депозита"""
    
    def __init__(self):
        self.lock = Lock()
        self.depo = 1000

    def deposite(self, amount):
        with self.lock:
            self.depo = self.depo + amount
            print(f"Deposited {amount}, new balance is {self.depo}")

    def withdraw(self, amount):
        with self.lock:
            self.depo = self.depo - amount
            print(f"Withdrew {amount}, new balance is {self.depo}")


def deposite_task(amount):
    for _ in range(5):
        account.deposite(amount)

def withdraw_task(amount):
    for _ in range(5):
        account.withdraw(amount)

account = BankAccount()

dep_t1 = Thread(target=deposite_task, args=(100,))
with_t1 = Thread(target=withdraw_task, args=(150,))

dep_t1.start()
with_t1.start()

dep_t1.join()
with_t1.join()


