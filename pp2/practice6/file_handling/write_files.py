def write_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    print("File written successfully!")


if __name__ == "__main__":
    write_file("example.txt", "Hello, this is a test file.")