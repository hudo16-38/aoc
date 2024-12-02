from dataclasses import dataclass

@dataclass
class Record:
    levels: list[int]

    def differences(self) -> list[int]:
        dffs = []
        for i in range(len(self.levels) - 1):
            dffs.append(self.levels[i+1] - self.levels[i])
        return dffs
    
    def is_increasing(self) -> bool:
        s = list(sorted(self.levels))
        return self.levels == s
    
    def is_decreasing(self) -> bool:
        s = list(sorted(self.levels, reverse=True))
        return self.levels == s
    
    def is_safe(self, one_out: bool = False) -> bool:
        if not one_out:
            if not (self.is_increasing() or self.is_decreasing()):
                return False
            
            if self.is_increasing():
                dffs = self.differences()
                return all(1 <= d <= 3 for d in dffs)
            
            dffs = self.differences()
            return all(-1 >= d >= -3 for d in dffs)
        for i in range(len(self.levels)):
            removed = self.levels.pop(i)
            check = self.is_safe()
            if check:
                return True
            self.levels.insert(i, removed)
        return False
    
def load_input(file: str) -> list[Record]:
    res = []
    with open(file, "r") as f:
        for line in f:
            levels = list(map(int, line.strip().split()))
            res.append(Record(levels))
    return res

def safe_count(records: list[Record], one_out: bool=False) -> int:
    return sum(r.is_safe(one_out) for r in records)

if __name__ == "__main__":
    #file = "test_input.txt"
    file = "my_input.txt"
    records = load_input(file)
    count = safe_count(records, True)
    print(f"{count = }")
