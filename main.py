from stats import count_words 
from stats import count_characters

def get_book_test(path):
    content = ""

    with open(path) as f:
        content = f.read()

    return content

def main():
    path_to_file = "./books/frankenstein.txt"
    book_content = get_book_test(path_to_file)
    word_count = count_words(book_content)
    characters_count = count_characters(book_content)
    print(f"{word_count} words found in the document")
    #count_characters(book_content)
    for c in characters_count:
        print(f"'{c}': {characters_count[c]}")

main()
