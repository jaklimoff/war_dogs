import random
import time
import sys
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    value = random.randint(1, 10000)
    clear()
    print """

    dsadasdasoidjasdjaskljdlkasj


    dsadasdasoidjasdjaskljdlkasj
    dsadasdasoidjasdjaskljdlkasj
    dsadas     {value}      kljdlkasj
    dsadasdasoidjasdjaskljdlkasj
    dsadasdasoidjasdjaskljdlkasj

    """.format(value=value)


    time.sleep(0.2)
