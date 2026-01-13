def get_count_words(book):
    split = book.split()
    return len(split)

def get_count_char(book):
    each_char = {}
    for char in book.lower():
        each_char[char] = each_char.get(char, 0) + 1
    return each_char