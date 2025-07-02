import sys
from stats import word_count, char_count, sorted_char_count

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    print("============ BOOKBOT ============")
    print(f" Analyzing book found at {book_path}...")  
    book_text = get_book_text(book_path)
    word_count(book_text)
    sorted_char_count(book_text)
    print("============= END ===============")

main()