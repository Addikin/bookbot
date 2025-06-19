def get_book_text(filepath):
    with open(filepath) as unread:
        opened_book = unread.read()
        return opened_book
def count_words(file_contents):
        words = file_contents.split()
        return len(words)
def count_characters(file_contents):
    word_amounts = {}
    characters = file_contents.lower()
    for character in characters:
        if character not in word_amounts:
            word_amounts[character] = 1
        else:
            word_amounts[character] += 1
    return word_amounts