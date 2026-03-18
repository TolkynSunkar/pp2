import os


def create_directory(dirname):
    os.makedirs(dirname, exist_ok=True)
    print("Directory created!")


def list_directory(path="."):
    print("Files and directories:")
    for item in os.listdir(path):
        print(item)


if __name__ == "__main__":
    create_directory("test_dir")
    list_directory()