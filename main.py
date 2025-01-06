def get_words_in_book(book):
    text = book.split()
    print(len(text))

def get_character_amount(book):
    lowercase_book = book.lower()

    character_amount = {}

    for char in lowercase_book:
        if not char.isalpha():
            pass
        elif char not in character_amount:
            character_amount[char] = 1
            continue
        else:
            character_amount[char] += 1
    return character_amount

def print_report(book, wordcount, character_amounts):
    print(f"--- Begin report of {book} ---")
    print(f"{wordcount} words found in the document")
    print("")
    for key, value in character_amounts.items():
        print(f"The '{key}' character was found {value} times")
    print("--- End report ---")
    
def main():
    book_to_read = "./books/frankenstein.txt"
    with open(book_to_read) as f:
        file_contents = f.read()
        wordcount = get_words_in_book(file_contents)
        character_amounts = get_character_amount(file_contents)
        print_report(book_to_read, wordcount, character_amounts)

if __name__ == "__main__":
    main()

