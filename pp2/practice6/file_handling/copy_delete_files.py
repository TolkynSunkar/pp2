import shutil
import os


def copy_file(source, destination):
    shutil.copy(source, destination)
    print("File copied!")


def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print("File deleted!")
    else:
        print("File does not exist!")


if __name__ == "__main__":
    copy_file("example.txt", "copy_example.txt")
    delete_file("copy_example.txt")