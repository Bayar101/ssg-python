import os
import shutil


def get_path_dirs(path):
    abs_path = os.path.abspath(path)
    if os.path.exists(abs_path):
        list = os.listdir(abs_path)
        return abs_path, list
    else:
        raise Exception("Invalid path")


def action_remove(target_path, dirs):
    if len(dirs) == 0:
        return

    for dir in dirs:
        abs_path = os.path.join(target_path, dir)
        if os.path.exists(abs_path):
            if os.path.isfile(abs_path):
                # print(f"Delete file: {abs_path}")
                os.remove(abs_path)
            else:
                child_dirs = os.listdir(abs_path)
                for child in child_dirs:
                    action_remove(abs_path, [child])
                # print(f"Delete dir: {abs_path}")
                os.rmdir(abs_path)

        else:
            raise Exception(f"Invalid remove path {abs_path}")


def action_copy(source_path, dirs, target_path):
    if len(dirs) == 0:
        return
    for dir in dirs:
        abs_path = os.path.join(source_path, dir)
        dest_abs_path = os.path.join(target_path, dir)
        if os.path.exists(abs_path):
            if os.path.isfile(abs_path):
                # print(f"Copy file: {abs_path}")
                shutil.copy(abs_path, dest_abs_path)
            else:
                child_dirs = os.listdir(abs_path)
                # print(f"Create dir: {abs_path}")
                os.mkdir(dest_abs_path)
                for child in child_dirs:
                    action_copy(abs_path, [child], dest_abs_path)
        else:
            raise Exception("Invalid source path for copy")


def path_action(target_path, dirs, copy_dest=None):
    if copy_dest:
        action_copy(target_path, dirs, copy_dest)
    else:
        action_remove(target_path, dirs)


def static_to_public(dest="./docs", source="./static"):
    dest_abs_path, dest_dirs = get_path_dirs(dest)
    source_abs_path, source_dirs = get_path_dirs(source)

    path_action(dest_abs_path, dest_dirs)
    # print("———————————————")
    path_action(source_abs_path, source_dirs, dest_abs_path)

    return
