import inspect
import os
import shutil


def get_script_path(location):
    """Gets the scripts path"""
    path = inspect.getfile(location)
    general_path = os.path.dirname(path)
    return os.path.join(general_path, 'flask_app')


def copy(script_dir, destination):
    """Copy to directory

    Args:
        script_dir (dir): directory to copy from
        destination (dir): directory to copy to
    """
    full_path = os.path.dirname(os.path.abspath(destination))
    try:
        shutil.copytree(os.path.join(script_dir), destination)
        # create .env file
        shutil.copy(
            destination + "/.env.sample", destination + "/.env"
        )
        msg = f"\nCopy to {full_path} successfull\n"
        print("\033[92m {}\033[00m".format(msg))

    except FileExistsError:
        msg = f"Directory {full_path} already exists"
        print("\n\033[91m {}\033[00m\n".format(msg))
