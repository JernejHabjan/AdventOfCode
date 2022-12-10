from pprint import pprint
import numpy as np


def is_visible_from_top(trees: list[list[int]], row_idx: int, col_idx: int) -> bool:
    tree_height = trees[row_idx][col_idx]

    max_height = -1
    for visible_row_idx in range(0, row_idx):
        test_tree_height = trees[visible_row_idx][col_idx]
        if test_tree_height > max_height:
            max_height = test_tree_height
            if max_height > tree_height:
                return False
    return tree_height > max_height


def is_visible_from_bottom(trees: list[list[int]], row_idx: int, col_idx: int) -> bool:
    tree_height = trees[row_idx][col_idx]

    rows = len(trees)
    max_height = -1
    for visible_row_idx in range(row_idx + 1, rows):
        test_tree_height = trees[visible_row_idx][col_idx]
        if test_tree_height > max_height:
            max_height = test_tree_height
            if max_height > tree_height:
                return False
    return tree_height > max_height


def is_visible_from_left(trees: list[list[int]], row_idx: int, col_idx: int) -> bool:
    tree_height = trees[row_idx][col_idx]

    max_height = -1
    for visible_col_idx in range(col_idx):
        test_tree_height = trees[row_idx][visible_col_idx]
        if test_tree_height > max_height:
            max_height = test_tree_height
            if max_height > tree_height:
                return False
    return tree_height > max_height


def is_visible_from_right(trees: list[list[int]], row_idx: int, col_idx: int) -> bool:
    tree_height = trees[row_idx][col_idx]

    columns = len(trees[0])
    max_height = -1
    for visible_col_idx in range(col_idx + 1, columns):
        test_tree_height = trees[row_idx][visible_col_idx]
        # print("test right - printing test_tre_height", test_tree_height, row_idx, visible_col_idx)
        if test_tree_height > max_height:
            max_height = test_tree_height
            if max_height > tree_height:
                return False

    return tree_height > max_height


def is_visible_from_any_of_4_sides(trees: list[list[int]], row_idx: int, col_idx: int) -> bool:
    tree_height = trees[row_idx][col_idx]
    # print("visible tree to determine", tree_height)

    visible_top = is_visible_from_top(trees, row_idx, col_idx)
    visible_bottom = is_visible_from_bottom(trees, row_idx, col_idx)
    visible_left = is_visible_from_left(trees, row_idx, col_idx)
    visible_right = is_visible_from_right(trees, row_idx, col_idx)
    # print("visible from top", visible_top, "visible from bottom", visible_bottom, "visible from left", visible_left,
    #       "visible from right", visible_right)

    return visible_top or visible_bottom or visible_left or visible_right


def init_arrays():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    trees = []
    for line in lines:
        tree_line = [int(x) for x in list(line)]
        trees.append(tree_line)

    rows = len(trees)
    columns = len(trees[0])
    # pprint(trees)
    # print(rows, columns)

    visible_trees = np.full((columns, rows), 0)
    return trees, visible_trees, rows, columns


def aoc_2022_08_a():
    trees, visible_trees, rows, columns = init_arrays()

    for row_idx in range(rows):
        for col_idx in range(columns):
            if row_idx == 0 or row_idx == rows - 1 or col_idx == 0 or col_idx == columns - 1:
                visible_trees[col_idx, row_idx] = 1
                continue
            if is_visible_from_any_of_4_sides(trees, row_idx, col_idx):
                visible_trees[col_idx, row_idx] = 1
    # print(visible_trees)

    visible_sum = visible_trees.sum()

    return visible_sum


if __name__ == '__main__':
    print(aoc_2022_08_a())
