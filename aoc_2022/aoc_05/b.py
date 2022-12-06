from collections import deque
from .a import extract_crates_and_instructions


def move_crates_multiple_at_a_time(instruction: tuple[int, int, int], stacks: list[deque]):
    move_quantity, move_from, move_to = instruction
    move_from_stack = stacks[move_from - 1]
    move_to_stack = stacks[move_to - 1]

    intermediate_stack = deque()
    for i in range(move_quantity):
        item = move_from_stack.pop()
        intermediate_stack.append(item)
    intermediate_stack.reverse()
    for item in intermediate_stack:
        move_to_stack.append(item)


def aoc_2022_05_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    (stacks, instructions) = extract_crates_and_instructions(lines)

    for instruction in instructions:
        move_crates_multiple_at_a_time(instruction, stacks)

    message = ""
    for stack in stacks:
        item = stack.pop()
        message += item
    return message


if __name__ == '__main__':
    print(aoc_2022_05_b())
