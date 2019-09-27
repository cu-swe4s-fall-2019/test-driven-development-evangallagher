import math
import sys


def list_mean(L):

    if L is None:
        return None

    if len(L) == 0:
        return None

    try:
        mean = sum(L)/len(L)

    except TypeError:
        raise TypeError('Unexpected Value')

    return mean


def list_stdev(L):

    if L is None:
        return None

    if len(L) == 0:
        return None

    try:
        s = sum(L)/len(L)

    except TypeError:
        raise TypeError('Unexpected value')

    stdv = math.sqrt(sum([(s - x) ** 2 for x in L]) / (len(L) - 1))

    return stdv
