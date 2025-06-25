from stats import count_words 

def get_book_test(path):
    content = ""

    with open(path) as f:
        content = f.read()

    return content

def main():
    path_to_file = "./books/frankenstein.txt"
    book_content = get_book_test(path_to_file)
    word_count = count_words(book_content)
    print(f"{word_count} words found in the document")

main()