def count_words(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def count_char(book_text):
    char_counts = {}
    lower_chars = book_text.lower()
    for char in lower_chars:
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_chars(char_counts):
    chars_list = []
    for char, count in char_counts.items():
        if char.isalpha():
            chars_list.append({"char": char, "num": count})
    def sort_on(count):
        return count["num"]
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list



