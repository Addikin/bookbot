def get_book_text(filepath):
    with open(filepath) as unread:
        opened_book = unread.read()
        return opened_book
def count_words(file_contents):
        words = file_contents.split()
        return len(words)
def char_counts(file_contents):
    word_amounts = {}
    characters = file_contents.lower()
    for character in characters:
        if character not in word_amounts:
            word_amounts[character] = 1
        else:
            word_amounts[character] += 1
    return word_amounts
def sort_dict(dict):
    return dict["num"]
def sorted_dict(char_counts):
    final_dict = []
    for x in char_counts:
        if x.isalpha():
            before_final = {"char": x, "num": char_counts[x]}
            final_dict.append(before_final)
    final_dict.sort(reverse=True, key=sort_dict)
    return final_dict