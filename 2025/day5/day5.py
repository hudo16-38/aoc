from dataclasses import dataclass
from copy import deepcopy

class Database:

    @dataclass
    class IDRange:
        start: int
        end: int

        def __contains__(self, id: int) -> bool:
            return self.start <= id <= self.end

    def __init__(self, ranges: str) -> None:
        self.database = []

        ranges = ranges.splitlines()

        for r in ranges:
            beg, end = map(int, r.split("-"))
            self.database.append(self.IDRange(beg, end))

    def is_fresh(self, id: int) -> bool:
        for r in self.database:
            if id in r:
                return True
        return False
    
    def count_fresh(self, ids: list[int]) -> int:
        count = 0
        for id in ids:
            count += self.is_fresh(id)
        return count
    
    def number_of_fresh_ids(self) -> int:
        database = deepcopy(self.database)
        database.sort(key=lambda range: range.start)

        merged = [database[0]]

        for range in database[1:]:
            last_range = merged[-1]
            if range.start <= last_range.end:
                last_range.end = max(range.end, last_range.end)
            else:
                merged.append(range)
        count = 0
        for range in merged:
            count += range.end - range.start + 1
        return count


def load_input(file_name: str) -> tuple[str, str]:
    with open(file_name, "r") as f:
        return f.read().split("\nX\n")
    
def parse_input(text: str) -> tuple[str, list[int]]:
    database, ids = text.split("\n\n")
    ids = list(map(int, ids.splitlines()))
    return database, ids

if __name__ == "__main__":
    test_input, my_input = load_input("input.txt")

    d, ids = parse_input(test_input)
    d = Database(d)
    count = d.count_fresh(ids)
    print(count)
    num_fresh = d.number_of_fresh_ids()
    print(num_fresh)

    d, ids = parse_input(my_input)
    d = Database(d)
    count = d.count_fresh(ids)
    num_fresh = d.number_of_fresh_ids()
    print(count)
    print(num_fresh)
