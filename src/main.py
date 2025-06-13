import os
import shutil

SOURCE = "static"
TARGET = "public"

def main():
    print("static site generator v1.0.0")
    print("developed by: amir barak")

    static_dir, public_dir = initialize()

    clone_contents(static_dir)
    print("goodbye")


def initialize():
    static_dir = os.path.join(os.curdir, SOURCE)
    if not os.path.exists(static_dir):
        raise Exception(f"static directory missing from current location: {static_dir}")

    public_dir = os.path.join(os.curdir, TARGET)
    if os.path.exists(public_dir):
        print(f"deleting public dir: {public_dir}")
        shutil.rmtree(public_dir)
    
    return static_dir, public_dir


def clone_contents(source_dir):
    global SOURCE
    global TARGET
    target_dir = source_dir[len(SOURCE):]
    print(f"{source_dir} ---> {target_dir}")

    # dir_items = os.listdir(parent_dir)
    # for item in dir_items:
    #     subpath = os.path.join(parent_dir, item)
    #     if os.path.isdir(subpath):
    #         subpath += "/"

    #     print(f" {subpath}")

if __name__ == '__main__':
    main()
