#!/usr/bin/env python

import time
import random

print()

start = time.time()

for i in range(5):

    zahl1=random.randint(1,10)
    zahl2=random.randint(1,10)
    ergebniss= zahl1 * zahl2

    while True:

        tipp = int(input(f"Задача {i+1} :        {zahl1} * {zahl2} = "))

        if tipp==ergebniss:

            print("Правилно!")
            break
        else: print("Грешка! Опитай пак!")

end=int(time.time()-start)

print(f"Решихте задачите за {end} секунди!")