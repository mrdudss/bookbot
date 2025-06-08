from stats import get_num_words
from stats import count_characters
from stats import sorted_list
import sys
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_num_words(text)
    list_char = count_characters(text)
    sorted = sorted_list(list_char)
    print("============ BOOKBOT ============") 
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
         return f.read()

main()