#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    s = input()
    sList = list(s)
    a = list(set(sList))
    a.sort()
    my_dict = {}
    for i in a:
        my_dict[i] = sList.count(i)

    sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1], reverse=True))

    counter = 0
    prev = set()
    for key, value in sorted_dict.items():
        prev.add(value)
        counter += 1
        if (len(prev) >= 4) or (counter == 4):
            break
        print(key, value)
