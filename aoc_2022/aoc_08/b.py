import aoc_2022.aoc_08.a as aoc_08_a


def get_visibility_down(trees, row_idx, col_idx) -> int:
    tree_height = trees[row_idx][col_idx]
    rows = len(trees)
    visible_nr = 0
    for visible_row_idx in range(row_idx + 1, rows):
        test_tree_height = trees[visible_row_idx][col_idx]
        # print("down - printing tree height", tree_height, "and test tree height", test_tree_height)
        visible_nr += 1
        if test_tree_height >= tree_height:
            break

    # print("to test visibility down", tree_height, "of visible nr", visible_nr)
    return visible_nr


def get_visibility_up(trees, row_idx, col_idx) -> int:
    tree_height = trees[row_idx][col_idx]
    visible_nr = 0
    for visible_row_idx in range(row_idx-1, -1, -1):
        test_tree_height = trees[visible_row_idx][col_idx]
        # print("up - printing tree height", tree_height, "and test tree height", test_tree_height, "row_dx",
        #       visible_row_idx)
        visible_nr += 1
        if test_tree_height >= tree_height:
            break

    # print("to test visibility up", tree_height, "of visible nr", visible_nr)
    return visible_nr


def get_visibility_right(trees, row_idx, col_idx) -> int:
    tree_height = trees[row_idx][col_idx]
    cols = len(trees[0])
    visible_nr = 0
    for visible_col_idx in range(col_idx + 1, cols):
        test_tree_height = trees[row_idx][visible_col_idx]
        # print("right -printing tree height", tree_height, "and test tree height", test_tree_height)
        visible_nr += 1
        if test_tree_height >= tree_height:
            break

    # print("to test visibility right", tree_height, "of visible nr", visible_nr)
    return visible_nr


def get_visibility_left(trees, row_idx, col_idx) -> int:
    tree_height = trees[row_idx][col_idx]
    visible_nr = 0
    for visible_col_idx in range(col_idx-1, -1, -1):
        test_tree_height = trees[row_idx][visible_col_idx]
        # print("left - printing tree height", tree_height, "and test tree height", test_tree_height)
        visible_nr += 1
        if test_tree_height >= tree_height:
            break

    # print("to test visibility left", tree_height, "of visible nr", visible_nr)
    return visible_nr


def aoc_2022_08_b():
    trees, visibility_trees, rows, columns = aoc_08_a.init_arrays()

    for row_idx in range(rows):
        for col_idx in range(columns):
            if row_idx == 0 or row_idx == rows - 1 or col_idx == 0 or col_idx == columns - 1:
                visibility_trees[col_idx, row_idx] = 0
                continue

            visibility_down = get_visibility_down(trees, row_idx, col_idx)
            visibility_up = get_visibility_up(trees, row_idx, col_idx)
            visibility_left = get_visibility_left(trees, row_idx, col_idx)
            visibility_right = get_visibility_right(trees, row_idx, col_idx)

            # print("visibility for ", trees[row_idx][col_idx], "visibility_down", visibility_down, "visibility_up",
            #       visibility_up, "visibility_left", visibility_left, "visibility_right", visibility_right)
            visibility_trees[col_idx, row_idx] = visibility_down * visibility_up * visibility_left * visibility_right
            # print("#######################################")
    # print(visibility_trees)

    visibility_sum = visibility_trees.max()

    return visibility_sum


if __name__ == '__main__':
    print(aoc_2022_08_b())
