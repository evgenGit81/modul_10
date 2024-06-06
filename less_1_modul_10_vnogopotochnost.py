# -*- coding: utf-8 -*-
import time
import threading
"""первый вариант программы"""
def schetcthik(numlist):
    """Вывод цифр с интервалом 1 секунда"""
    for i in range(len(numlist)):
        print(numlist[i])
        time.sleep(1)

def alfavit(alflist):
    """Выводит буквы адфавита с интервалом 1 секунда"""
    for i in range(len(alflist)):
        print(alflist[i])
        time.sleep(1)

numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
alflist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
schk = threading.Thread(target=schetcthik, args=(numlist,))
alfschk = threading.Thread(target=alfavit, args=(alflist,))
schk.start()
alfschk.start()
schk.join()
alfschk.join()

