def load_input(file_name: str) -> tuple[str, str]:
    with open(file_name, "r") as f:
        test_input, my_input = f.read().split("\n\n")
        return test_input, my_input

def parse_input(text: str) -> tuple[tuple[int]]:
    return tuple(
        tuple(map(int, row)) for row in text.split("\n")
    )

def find_numbers(numbers: tuple[int], k:int) -> int:
    s = []
    skips = len(numbers) - k

    for num in numbers:
        while s and num > s[-1] and skips > 0:
            s.pop()
            skips -= 1
        s.append(num)

    solution = map(str, s[:k])
    return int("".join(solution))
        



def total_joltage(text: str, k: int) -> int:
    rows = parse_input(text)
    s = 0
    for numbers in rows:
        best = find_numbers(numbers, k)
        s += best
    return s

if __name__ == "__main__":
    test_input, my_input = load_input("input.txt")
    
    s = total_joltage(test_input, 2)
    print(s)

    s = total_joltage(my_input, 2)
    print(s)

    s = total_joltage(test_input, 12)
    print(s)

    s = total_joltage(my_input, 12)
    print(s)

