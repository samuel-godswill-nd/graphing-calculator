#!/usr/bin/env python3

import sys

def add(x: int, y: int) -> int:
    return x + y

if __name__ == '__main__':
    print(add(int(sys.argv[1]), int(sys.argv[2]))) 
