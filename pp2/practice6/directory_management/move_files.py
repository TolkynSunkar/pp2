import shutil


def move_file(source, destination):
    shutil.move(source, destination)
    print("File moved!")


if __name__ == "__main__":
    move_file("example.txt", "test_dir/example.txt")