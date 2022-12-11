import math


class Tail:
    _current_x = 0
    _current_y = 0
    visited_coordinates: set[tuple[int, int]] = [(_current_x, _current_y)]

    def move_tail_next_to_head(self, head_x, head_y, prev_head_x, prev_head_y, direction):
        dist = math.dist([head_x, head_y], [self._current_x, self._current_y])
        print("new head_x", head_x, "new head_y", head_y, "_current_x", self._current_x, "_current_y", self._current_y,
              "DIST:",
              dist)

        if dist == 1:
            return

        are_touching = dist < 2

        same_row_or_col = head_x == self._current_x or head_y == self._current_y

        if not are_touching:
            if not same_row_or_col:
                # move diagonally
                new_x = prev_head_x  # todo
                new_y = prev_head_y  # todo
                print("not touching and diff row or col")

            else:
                print("not touching and same row or col")
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
        else:
            if not same_row_or_col:
                print("are touching and not same row and col")
                # todo move diagonally if lagging behind
                new_x = self._current_x  # todo
                new_y = self._current_y  # todo

            else:
                print("are touching and same row and col")
                new_x = self._current_x  # todo
                new_y = self._current_y  # todo

        self._current_x = new_x
        self._current_y = new_y

        self.visited_coordinates.add((self._current_x, self._current_y))

    def get_debug_pos(self):
        return self._current_x, self._current_y


class Head:
    _current_x = 0
    _current_y = 0
    _tail = Tail()

    def move_head_multiple_steps(self, direction, amount):
        if direction == "R":
            increase_factor = (1, 0)
        elif direction == "L":
            increase_factor = (-1, 0)
        elif direction == "U":
            increase_factor = (0, -1)
        else:  # direction "D"
            increase_factor = (0, 1)

        move_x, move_y = increase_factor
        for i in range(amount):
            new_x = self._current_x + move_x
            new_y = self._current_y + move_y
            self._move_head(new_x, new_y, direction)

    def _move_head(self, new_x, new_y, direction):
        prev_head_x = self._current_x
        prev_head_y = self._current_y
        self._current_x = new_x
        self._current_y = new_y
        self._tail.move_tail_next_to_head(self._current_x, self._current_y, prev_head_x, prev_head_y, direction)

    def get_tail_visited_coordinates_count(self) -> int:
        return len(self._tail.visited_coordinates)

    def get_tail_visited_coordinates(self):
        return self._tail.visited_coordinates

    def get_debug_pos(self):
        return self._current_x, self._current_y

    def get_debug_pos_tail(self):
        return self._tail.get_debug_pos()


def aoc_2022_09_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    movements: list[tuple[str, int]] = []
    for line in lines:
        movements.append((line[0], int(line[2])))

    head = Head()
    for direction, amount in movements:
        head.move_head_multiple_steps(direction, amount)
        print("#################### Head debug pos", head.get_debug_pos(), "tail debug pos", head.get_debug_pos_tail(),
              "tail coordinates",
              head.get_tail_visited_coordinates())

    visited_count = head.get_tail_visited_coordinates_count()

    return visited_count


if __name__ == '__main__':
    print(aoc_2022_09_a())
