def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
    return file_content

def get_count_words(book):
    split = book.split()
    return len(split)
    

def main():
    path = "books/frankenstein.txt"
    content = get_book_text(path)
    print(content)
    num_words = get_count_words(content)
    print(f"Found {num_words} total words")

main()