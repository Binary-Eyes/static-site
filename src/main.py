import os
import sys
import shutil
from page import *


def main():
    print("static site generator v1.0.0")
    print("developed by: amir barak")
    basepath = get_base_path(sys.argv)
    static_dir, public_dir = initialize()
    clone_contents(static_dir)
    generate_pages_recursive(basepath, "./content", "./template.html", public_dir)

    print("goodbye")


def get_base_path(args):
    if len(args) == 0:
        return "/"
    
    return args[0]


def initialize():
    static_dir = os.path.join(os.curdir, "static")
    if not os.path.exists(static_dir):
        raise Exception(f"static directory missing from current location: {static_dir}")

    public_dir = os.path.join(os.curdir, "public")
    if os.path.exists(public_dir):
        print(f"deleting public dir: {public_dir}")
        shutil.rmtree(public_dir)
    
    return static_dir, public_dir


def clone_contents(source_dir):
    target_dir = source_dir.replace("static", "public")
    print(f"{source_dir} ---> {target_dir}")
    if not os.path.exists(target_dir):
        os.mkdir(target_dir)

    source_items = os.listdir(source_dir)
    for item in source_items:
        source_path = os.path.join(source_dir, item)
        target_path = os.path.join(target_dir, item)
        if os.path.isdir(source_path):
            clone_contents(source_path)
        else:
            print(f"{source_path} ---> {target_path}")
            shutil.copy(source_path, target_path)


if __name__ == '__main__':
    main()
