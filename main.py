def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    char_list = [
        {"char": char, "num": num} for char, num in count_characters(text).items()
    ]
    char_list.sort(key=sort_on, reverse=True)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    for item in char_list:
        print(f"The '{item['char']}' character was found {item['num']} times")
    print("\n--- End report ---")


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
        if not char.isalpha():
            continue
        if char in my_dict:
            my_dict[char] += 1
        else:
            my_dict[char] = 1
    return my_dict


def sort_on(dict):
    return dict["num"]


if __name__ == "__main__":
    main()
