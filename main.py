from stats import get_num_words
from stats import count_characters

def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    num_words = get_num_words(text)
    list_char = count_characters(text)
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print()#sorted list
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
         return f.read()

main()