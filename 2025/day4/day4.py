class Grid:
    def __init__(self, grid_text: str) -> None:
        self.grid = [list(row) for row in grid_text.splitlines()]
        self.height, self.width = len(self.grid), len(self.grid[0])

    def neighbours(self, y: int, x: int) -> list[tuple[int, int]]:
        neighbourhood = []

        for pos_y in y-1, y, y+1:
            for pos_x in x-1, x, x+1:
                neighbourhood.append((pos_x, pos_y))
        res = []
        for pos_x, pos_y in neighbourhood:
            if - 1 < pos_x < self.width:
                if -1 < pos_y < self.height:
                    res.append((pos_x, pos_y)) 

        res.remove((x, y))
        return res

    
    def is_accessible(self, x: int, y: int) -> bool:
        if self.grid[y][x] == ".":
            return False
        count = 0

        for pos_x, pos_y in self.neighbours(y, x):
            count += self.grid[pos_y][pos_x] == "@"


        return count < 4
    
    def get_accessible(self) -> list[tuple[int, int]]:
        res = []

        for y in range(self.height):
            for x in range(self.width):
                if self.is_accessible(x, y):
                    res.append((x, y))
        return res
    
    def count_accessible(self) -> int:
        return len(self.get_accessible())
    
    def remove_accessible(self) -> int:
        accessible = self.get_accessible()
        count = len(accessible)

        while accessible:
            for x, y in accessible:
                self.grid[y][x] = "."
            accessible = self.get_accessible()
            count += len(accessible)

        return count
    

def load_input(file_name: str) -> tuple[str, str]:
    with open(file_name, "r") as f:
        return f.read().split("\n\n")
    

if __name__ == "__main__":
    test_input, my_input = load_input("input.txt")

    grid1 = Grid(test_input)
    grid2 = Grid(my_input)

    count = grid1.count_accessible()
    print(count)
    count = grid1.remove_accessible()
    print(count)

    count = grid2.count_accessible()
    print(count)
    count = grid2.remove_accessible()
    print(count)
