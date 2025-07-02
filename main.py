from stats import word_count, char_count

def get_book_text(book_path):
    with open(book_path) as file:
        return file.read()
    
def main():
    book_path = 'books/frankenstein.txt' 
    book_text = get_book_text(book_path)
    word_count(book_text)
    char_count(book_text)

main()