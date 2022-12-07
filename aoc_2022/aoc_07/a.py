from __future__ import annotations


class Directory:
    def __init__(self, name, parent_dir: Directory | None):
        self.name = name
        self.files_and_folders = []
        self.parent_dir = parent_dir


class File:
    def __init__(self, name, size: int, parent_dir: Directory | None):
        self.name = name
        self.size = size
        self.parent_dir = parent_dir


def debug_print_directory(current_dir: Directory, current_level: int):
    indent = current_level * " "
    print(indent + "- " + current_dir.name + " (dir)")
    for file_and_folder in current_dir.files_and_folders:
        indent_children = (current_level + 2) * " "
        if isinstance(file_and_folder, Directory):
            debug_print_directory(file_and_folder, current_level + 1)
        else:
            print(indent_children + "- " + file_and_folder.name + " (file, size=" + str(file_and_folder.size) + ")")


valid_size = 0


def get_directory_sum_size(current_dir: Directory, max_size=100000) -> int:
    # todo remove this global var
    global valid_size
    total_size = 0
    for file_and_folder in current_dir.files_and_folders:
        if isinstance(file_and_folder, Directory):
            size = get_directory_sum_size(file_and_folder)
            print(size, file_and_folder.name)
            total_size += size
        else:
            total_size += file_and_folder.size
            print(file_and_folder.size, file_and_folder.name)
    # if total_size > max_size:
    #     total_size = 0

    print("returning total size", current_dir.name, total_size)
    if total_size <= max_size:
        print("valid size", total_size)
        valid_size += total_size
    return total_size


def aoc_2022_07_a():
    import pathlib
    with open(str(pathlib.Path(__file__).parent.resolve()) + '\\input.txt', "r") as f:
        lines = f.read().splitlines()

    root_dir = Directory("/", None)
    current_dir = root_dir
    for line in lines:
        args = line.split(" ")
        if args[0] == "$":
            command_arg = args[1]
            if command_arg == "ls":
                continue
            elif command_arg == "cd":
                path = args[2]
                if path == "/":
                    current_dir = root_dir
                elif path == "..":
                    if current_dir.parent_dir is not None:
                        current_dir = current_dir.parent_dir
                else:
                    new_dir = next((x for x in current_dir.files_and_folders if x.name == path), None)
                    current_dir = new_dir
        else:
            if args[0] == "dir":
                current_dir.files_and_folders.append(Directory(args[1], current_dir))
            else:
                current_dir.files_and_folders.append(File(args[1], int(args[0]), current_dir))
    debug_print_directory(root_dir, 0)

    get_directory_sum_size(root_dir)
    return valid_size


if __name__ == '__main__':
    print(aoc_2022_07_a())
