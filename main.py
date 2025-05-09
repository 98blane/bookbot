from stats import count_words
from stats import count_char
from stats import sort_chars
import sys
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    num_chars = count_char(book_text)
    sorted_chars = sort_chars(num_chars)

    print(f"Found {num_words} total words")
    print(num_chars)
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")

main()
