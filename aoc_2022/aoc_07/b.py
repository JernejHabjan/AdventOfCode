import aoc_2022.aoc_07.a as aoc_07_a


def get_directory_sum_size(current_dir: aoc_07_a.Directory, directory_sizes: list[int]) -> int:
    total_size = 0
    for file_and_folder in current_dir.files_and_folders:
        if isinstance(file_and_folder, aoc_07_a.Directory):
            size = get_directory_sum_size(file_and_folder, directory_sizes)
            # print(size, file_and_folder.name)
            total_size += size
        else:
            total_size += file_and_folder.size
            # print(file_and_folder.size, file_and_folder.name)

    print("returning total size", current_dir.name, total_size)
    directory_sizes.append(total_size)
    return total_size


def aoc_2022_07_b():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    root_dir = aoc_07_a.create_dir_tree(lines)
    # debug_print_directory(root_dir, 0)

    total_disk_space = 70000000
    dir_sizes = []
    space_used = get_directory_sum_size(root_dir, dir_sizes)
    print("dir sizes", dir_sizes)
    remaining_space = total_disk_space - space_used
    print("remaining space", remaining_space)
    dir_sizes.sort()
    res = 0
    for size in dir_sizes:
        if size >= remaining_space:
            res = size
            break
    return res


if __name__ == '__main__':
    print(aoc_2022_07_b())
