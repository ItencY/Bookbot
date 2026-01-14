from stats import get_count_words, get_count_char, chars_dict_to_sorted_list
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    content = get_book_text(path)
    num_words = get_count_words(content)
    each_char = get_count_char(content)
    chars_sorted_list = chars_dict_to_sorted_list(each_char)
    # Print the report
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    
    print("============= END ===============")

main()