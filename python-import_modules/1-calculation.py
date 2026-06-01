#!/usr/bin/python3
from calculator_1 import add, vurma, bolme, cixma
a = 10
b = 5
if __name__ == "__main__":
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} * {} = {}".format(a, b, vurma(a, b)))
    print("{} / {} = {}".format(a, b, bolme(a, b)))
    print("{} - {} = {}".format(a, b, cixma(a, b)))
