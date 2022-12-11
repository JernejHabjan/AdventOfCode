import aoc_2022.aoc_09.a as aoc_09_a


def aoc_2022_09_b():
    movements = aoc_09_a.prepare_movements()
    head = aoc_09_a.Head()
    tails: list[aoc_09_a.Tail] = [aoc_09_a.Tail() for _ in range(9)]
    print(tails)
    for direction, amount in movements:
        for _ in range(amount):
            prev_head_x, prev_head_y = head.current_x, head.current_y
            head.move_head(direction)

            prev_current_tail_x, prev_current_tail_y = tails[0].current_x, tails[0].current_y
            tails[0].move_tail(head.current_x, head.current_y, prev_head_x, prev_head_y, direction)

            for i in range(1, 9):
                tails[i].move_tail(tails[i - 1].current_x, tails[i - 1].current_y, prev_current_tail_x,
                                   prev_current_tail_y, direction)

    visited_count = len(tails[8].visited_coordinates)

    return visited_count


if __name__ == '__main__':
    print(aoc_2022_09_b())
