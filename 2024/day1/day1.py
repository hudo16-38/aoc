import numpy as np
from collections import defaultdict, Counter

def load_input(file: str) -> tuple[np.array]:
    left, right = [], []
    with open(file, "r") as f:
        for line in f:
            x, y = line.strip().split()
            left.append(int(x))
            right.append(int(y))

    left.sort(); right.sort()
    return np.array(left), np.array(right)

def distance(left: np.array, right: np.array) -> int:
    return np.sum(np.abs(left - right))

def similarity(left: np.array, right: np.array) -> int:
    counter = Counter(right)
    s = 0

    for x in left:
        if x in counter:
            s += x*counter[x]
    return s

if __name__ == "__main__":
    #file = "test_input.txt"
    file = "my_input.txt"
    left, right = load_input(file)
    d = distance(left, right)
    s = similarity(left, right)
    print(f"{d = }")
    print(f"{s = }")