def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")
    print(count_characters(text))

def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()


def count_characters(text):
    lowercase_text = text.lower()
    my_dict = {}
    for char in lowercase_text:
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


if __name__ == '__main__':
    main()
