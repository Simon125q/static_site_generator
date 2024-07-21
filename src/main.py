import os
import shutil

from page_generator import generate_page

def copy_and_override_directory(path_from: str, path_to: str) -> None:
    if os.path.isdir(path_to):
        shutil.rmtree(path_to)
    copy_directory(path_from, path_to)


def copy_directory(path_from: str, path_to: str) -> None:
    input_dir = os.listdir(path_from)
    if not os.path.isdir(path_to):
        os.mkdir(path_to)
    for dir in input_dir:
        path_in = os.path.join(path_from, dir)
        path_out = os.path.join(path_to, dir)
        if os.path.isfile(path_in):
            shutil.copy(path_in, path_out)
        else:
            copy_directory(path_in, path_out)

def main() -> None:
    copy_and_override_directory("./static", "./public")
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()
