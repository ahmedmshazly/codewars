import math


def solution(array_a, array_b):
    temb = []
    for i, j in zip(array_a, array_b):
        temb.append(abs(i-j)**2)
    return sum(temb)/len(temb)

