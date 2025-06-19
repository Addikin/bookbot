from stats import count_words, get_book_text, count_characters
def main():
    filepath = "books/frankenstein.txt"
    file_contents = get_book_text(filepath)
    word_count = count_words(file_contents)
    print(f"{word_count} words found in the document")
    character_contents = count_characters(file_contents)
    print(character_contents)

main()