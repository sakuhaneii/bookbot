def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_dict = get_char_dict(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    for c in char_dict:
        print(f"The '{c}' character was found {char_dict[c]} times")

    print("--- End Report ---")


def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_dict(text):
    alphabet = list("abcdefghijklmnopqrstuvwxyz")
    chars = {}
    for letter in alphabet:
        chars[letter] = 0
    for c in text:
        lower_char = c.lower()
        if lower_char in alphabet:
            chars[lower_char] += 1
    return chars


main()