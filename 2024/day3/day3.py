import re

def load_input(file) -> str:
    with open(file, "r") as f:
        return f.read().strip()
    
def parse_commands(text: str) -> list[re.Match]:
    pattern = r"mul\(\d+,\d+\)"
    occurances = list(re.finditer(pattern, text))
    return occurances

def multiply(command: str) -> int:
    def mul(x,y): return x*y

    return eval(command, {"mul":mul})

def sum_commands(commands: list[str]) -> int:
    return sum(multiply(command.group(0)) for command in commands)

def find_conditiones(text: str) -> list[re.Match]:
    control_pattern = r"(do\(\)|don\'t\(\))"
    return list(re.finditer(control_pattern, text))

def sum_conditioned_commands(text: str) -> int:
    last_condition = True
    s = 0

    conditiones = find_conditiones(text)
    commands = parse_commands(text)
    tokens = conditiones + commands
    tokens.sort(key = lambda x: x.span())

    for token in tokens:
        if token.group(0) == "don't()":
            last_condition = False
        elif token.group(0) == "do()":
            last_condition = True
        elif last_condition:
            s += multiply(token.group(0))
    return s



if __name__ == "__main__":
    text = load_input("test_input.txt")
    occurances = parse_commands(text)
    #print(occurances)
    s = sum_commands(occurances)
    print(f"{s = }")
    text = load_input("my_input.txt")
    occurances = parse_commands(text)
    s = sum_commands(occurances)
    print(f"{s = }")
    ##################-PART2-######################
    text = load_input("test_input.txt")
    #print(text)
    conditiones = find_conditiones(text)
    #print(conditiones)
    s = sum_conditioned_commands(text)
    print(s)

    text = load_input("my_input.txt")
    s = sum_conditioned_commands(text)
    print(s)

