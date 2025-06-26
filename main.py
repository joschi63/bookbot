from stats import count_words 
from stats import count_characters
from stats import sort_character_dic

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
    new_counter = sort_character_dic(characters_count)

    print("============ BOOKBOT ============")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for n in new_counter:
        print(f"{n['character']}: {n['count']}")
    
    """
    count_characters(book_content)
    for c in characters_count:
        print(f"'{c}': {characters_count[c]}")
    """

main()
