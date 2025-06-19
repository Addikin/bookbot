import sys
from stats import count_words, get_book_text, char_counts, sorted_dict
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]
    file_contents = get_book_text(filepath)
    word_count = count_words(file_contents)
    character_contents = char_counts(file_contents)
    final_dict = sorted_dict(character_contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print(f"----------- Word Count -----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count ---------")
    for dictionary in final_dict:
        print(f"{dictionary['char']}: {dictionary['num']}")
    print("============= END =============")
main()