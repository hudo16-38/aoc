from dataclasses import dataclass

@dataclass
class IDRange:
    first_id: int
    last_id: int

    def get_invalid_ids(self, check_any: bool) -> list[int]:
        res = []
        for id in range(self.first_id, self.last_id+1):
            id = str(id)
            if len(id) == 1: continue
            if not check_any:
                if len(id) % 2 == 0:
                    size = len(id) // 2
                    slices = self.__slices(id, size)
                    if len(slices) == 1:
                        res.append(int(id))
            else:
                is_valid = True
                for size in reversed(range(1, len(id)//2 + 1)):
                    if len(id) % size == 0:
                        slices = self.__slices(id, size)
                        if len(slices) == 1:
                            is_valid = False
                            break
                if not is_valid:
                    res.append(int(id))
          
        return res
    
    def __slices(self, id: str, size: int) -> set[str]:
        return {id[i:i+size] for i in range(0, len(id), size)}
    
    

def load_input(file_name: str) -> tuple[str, str]:
    with open(file_name, "r") as f:
        test_input, my_input = f.read().split("\n\n")
        return test_input.replace("\n", ""), my_input.replace("\n", "")
    
def parse_input(ranges: str) -> list[IDRange]:
    ranges = ranges.split(",")
    res = []
    for r in ranges:
        first, last = r.split("-")
        id_range = IDRange(int(first), int(last))
        res.append(id_range)
    return res

def sum_invalid_ids(ranges: str, check_any: bool=False) -> int:
    s = 0
    id_ranges = parse_input(ranges)
    for r in id_ranges:
        s += sum(r.get_invalid_ids(check_any))
    return s

if __name__ == "__main__":
    test_input, my_input = load_input("input.txt")

    s = sum_invalid_ids(test_input)
    print(f"{s = }")

    s = sum_invalid_ids(my_input)
    print(f"{s = }")

    s = sum_invalid_ids(test_input, True)
    print(f"{s = }")

    s = sum_invalid_ids(my_input, True)
    print(f"{s = }")

