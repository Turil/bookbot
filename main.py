def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_words = count_words(text)
    print(f"{num_words} words found in the document")

def count_words(text):
    words = text.split()
    return len(words)

def get_text(path):
    with open(path) as f:
        return f.read()

if __name__ == '__main__':
    main()
