from stats import get_num_words, get_character_count, get_ordered_characters
import sys

def get_book_text(filepath):
    with open(filepath) as frankenstein_txt:
        text = frankenstein_txt.read()
    return text

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    
    words_counter = get_num_words(text)
    char_counter = get_character_count(text)
    report = get_ordered_characters(char_counter)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words_counter} total words")
    print("--------- Character Count -------")
    for item in report:
        if item["char"].isalpha(): #/.isalpha/ - checks if the characters are letters
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()

