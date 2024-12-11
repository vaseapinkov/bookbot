def get_word_count(text):
    return len(text.split(' '))

def get_character_count(text):
    characters = dict()
    text = text.lower()

    for ch in text:
        if not ch.isalpha():
            continue

        if ch not in characters:
            characters[ch] = 1
        else:
            characters[ch] += 1

    return characters

def get_book_text(path):
    with open(path, 'r') as f:
        return f.read()

def print_report(path, words_count, characters_count):
    print(f"--- Begin report of book {path} ---")
    print(f"{words_count} found in the document")
    print()
    for ch in characters_count:
        print(f"The '{ch}' character was found {characters_count[ch]} times")
    print("--- End report ---")


def main():
    path = './books/frankenstein.txt'
    text = get_book_text(path)
    words_count = get_word_count(text)
    characters_count = get_character_count(text)

    print_report(path, words_count, characters_count)

main()
