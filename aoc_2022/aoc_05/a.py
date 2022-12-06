from collections import deque


def extract_crates_and_instructions(lines: list[str]) -> (list[tuple[int, int, int]], list[deque]):
    import math
    started_extracting_instructions = False

    # instructions include "idx", "from", "to"
    instructions: list[tuple[int, int, int]] = []
    stacks: list[deque] = []
    for line in lines:
        if line == "":
            started_extracting_instructions = True
            continue

        if started_extracting_instructions:
            split_instructions = line.split(" ")
            instructions.append((int(split_instructions[1]), int(split_instructions[3]), int(split_instructions[5])))
        else:
            crate_str_length = 4
            for i in range(len(line)):
                crate_index = math.floor(i / crate_str_length)
                if len(stacks) < crate_index + 1:
                    stacks.append(deque())
                crate_letter_index = i % crate_str_length

                if crate_letter_index == 1:
                    crate_letter = line[i]
                    if not crate_letter.isdigit() and crate_letter != " ":
                        stacks[crate_index].append(crate_letter)
    for stack in stacks:
        stack.reverse()
    return stacks, instructions


def move_crates_one_at_a_time(instruction: tuple[int, int, int], stacks: list[deque]):
    move_quantity, move_from, move_to = instruction
    move_from_stack = stacks[move_from - 1]
    move_to_stack = stacks[move_to - 1]
    for i in range(move_quantity):
        item = move_from_stack.pop()
        move_to_stack.append(item)


def aoc_2022_05_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    (stacks, instructions) = extract_crates_and_instructions(lines)

    for instruction in instructions:
        move_crates_one_at_a_time(instruction, stacks)

    message = ""
    for stack in stacks:
        item = stack.pop()
        message += item
    return message


if __name__ == '__main__':
    print(aoc_2022_05_a())
