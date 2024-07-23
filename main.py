def main():
    with open(file="books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)


if __name__ == '__main__':
    main()
