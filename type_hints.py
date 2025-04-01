from typing import *
from collections import OrderedDict, deque, NamedTuple

x = 10      # type: int

def f(x: int ,y: int) -> int:
    return x + y

x = {}      # type: OrderedDict

def g(x: Sequence):
    print(len(x))
    print(x[2])
    for i in x:
        print(i)
    print() 

g([10,20,30])

hts = [97.1, 102.5, 97.5]                           # type: List[float]
person = ("Raymond", 5 * 12 + 11)                   # type: Tuple[str, float]
info = ("Perso", "Course", "Python", "Raymond")     # type: Tuple[str, ...]
fifo = deque()                                      # type: deque

# Point = NamedTuple("Point", [("x": int), ("y": int)])