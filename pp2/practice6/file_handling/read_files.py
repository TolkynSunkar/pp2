def read_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("File not found!")


if __name__ == "__main__":
    read_file("example.txt")