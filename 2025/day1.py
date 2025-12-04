def load_input(file_name: str) -> tuple[str, str]:
    with open(file_name, "r") as f:
        test_input, my_input = f.read().split("\n\n")
        return test_input.strip(), my_input.strip()

def turn_dial(dial: int, command: str, counter: int) -> tuple[int, int]:
    command, value = command[0], int(command[1:])
    # print(dial, command, value, counter)

    if command == "L":
        circles = value // 100
        counter += circles
        value %= 100
        if value >= dial and dial != 0: counter += 1
        dial -= value
        # print(dial % 100, counter)
        return dial % 100, counter
    
    circles = value // 100
    counter += circles
    value %= 100
    if value >= 100 - dial: counter += 1
    dial += value
    # print(dial % 100, counter)
    return dial % 100, counter

def split_commands(commands: str) -> list[str]:
    return commands.split("\n")

def run_commands(commands: str) -> int:
    dial, counter = 50, 0
    commands = split_commands(commands)
    for command in commands:
        dial, counter = turn_dial(dial, command, counter)
    return dial, counter

if __name__ == "__main__":
    #print(run_commands("L50\nR50"))
    test_input, my_input = load_input("input.txt")
    dial, counter = run_commands(test_input)
    print(f"Test dial: {dial}, test counter: {counter}")

    dial, counter = run_commands(my_input)
    print(f"My dial: {dial}, my counter: {counter}")