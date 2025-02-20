import os


def print_tree_structure(root_dir, level=0, max_depth=3, max_items=2, prefix=""):
    if level > max_depth:
        return

    items = os.listdir(root_dir)
    items_to_show = items[:max_items] + \
        (["..."] if len(items) > max_items else [])

    for idx, item in enumerate(items_to_show):
        item_path = os.path.join(root_dir, item)
        is_last_item = (idx == len(items_to_show) - 1)

        if os.path.isdir(item_path):
            print(f"{prefix}{'└── ' if is_last_item else '├── '}{item}/")
            # Recurse into the subdirectory with the appropriate prefix
            new_prefix = f"{prefix}{'    ' if is_last_item else '│   '}"
            print_tree_structure(item_path, level + 1,
                                 max_depth, max_items, new_prefix)
        else:
            print(f"{prefix}{'└── ' if is_last_item else '├── '}{item}")


# 替换为你的数据目录路径
root_directory = 'data'
print_tree_structure(root_directory)
