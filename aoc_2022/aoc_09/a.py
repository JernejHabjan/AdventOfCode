import math


class Tail:
    current_x = 0
    current_y = 0
    visited_coordinates: set[tuple[int, int]] = set()

    def __init__(self):
        self.visited_coordinates.add((self.current_x, self.current_y))

    def move_tail(self, head_x, head_y, prev_head_x, prev_head_y, direction):
        dist = math.dist([head_x, head_y], [self.current_x, self.current_y])
        # print("new head_x", head_x, "new head_y", head_y, "_current_x", self._current_x, "_current_y",
        # self._current_y, "DIST:", dist)

        if dist == 1:
            return

        are_touching = dist < 2

        same_row_or_col = head_x == self.current_x or head_y == self.current_y

        if are_touching:
            new_x = self.current_x
            new_y = self.current_y
        else:
            if not same_row_or_col:
                # move diagonally
                new_x = prev_head_x
                new_y = prev_head_y

            else:
                # print("not touching and same row or col")
                # same row or column - THIS IS OK
                if direction == "R":
                    new_x = head_x - 1
                    new_y = head_y
                elif direction == "L":
                    new_x = head_x + 1
                    new_y = head_y
                elif direction == "U":
                    new_x = head_x
                    new_y = head_y + 1
                else:  # direction "D"
                    new_x = head_x
                    new_y = head_y - 1

        self.current_x = new_x
        self.current_y = new_y

        self.visited_coordinates.add((self.current_x, self.current_y))

    def get_debug_pos(self):
        return self.current_x, self.current_y


class Head:
    current_x = 0
    current_y = 0

    def move_head(self, direction):
        if direction == "R":
            increase_factor = (1, 0)
        elif direction == "L":
            increase_factor = (-1, 0)
        elif direction == "U":
            increase_factor = (0, -1)
        else:  # direction "D"
            increase_factor = (0, 1)

        move_x, move_y = increase_factor

        self.current_x += move_x
        self.current_y += move_y

    def get_debug_pos(self):
        return self.current_x, self.current_y


def prepare_movements():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    movements: list[tuple[str, int]] = []
    for line in lines:
        a, b = line.split()
        movements.append((a, int(b)))
    return movements


def aoc_2022_09_a():
    movements = prepare_movements()
    head = Head()
    tail = Tail()
    for direction, amount in movements:
        for _ in range(amount):
            prev_head_x, prev_head_y = head.current_x, head.current_y
            head.move_head(direction)
            tail.move_tail(head.current_x, head.current_y, prev_head_x, prev_head_y, direction)

    visited_count = len(tail.visited_coordinates)

    return visited_count


if __name__ == '__main__':
    print(aoc_2022_09_a())
