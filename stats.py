def get_count_words(book):
    split = book.split()
    return len(split)

def get_count_char(book):
    each_char = {}
    for char in book.lower():
        each_char[char] = each_char.get(char, 0) + 1
    return each_char

def sort_on(dict):
    return dict["num"]

def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for char in num_chars_dict:
        sorted_list.append({"char": char, "num": num_chars_dict[char]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list