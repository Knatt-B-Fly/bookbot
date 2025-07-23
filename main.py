import sys
from stats import get_num_words, get_num_characters


def main():
    # Here you decide which file to read from a specified path
    book_path = "./workspace/github.com/bootdotdev/curriculum/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_num_characters(text)
    print(f"{num_words} words found in the document")
    print(chars_dict)

def get_book_text(filepath):
    # opens file specified at end of relative path
    with open(filepath) as f:
            book_contents = f.read()
            return book_contents




main()  


        
    