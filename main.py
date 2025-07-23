def main():
    # Here you decide which file to read from a specified path
    book_path = "./workspace/github.com/bootdotdev/curriculum/bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")


def get_book_text(filepath):
    # opens file specified at end of relative path
    with open(filepath) as f:
            book_contents = f.read()
            return book_contents

def get_num_words(text):
    words = text.split()
    return len(words)
     


main()  


        
    