def main():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    words = count_words(book_text)
    chars = count_chars(book_text)
    char_list = char_layout(chars)
    print(f"--- Begin report of {book_path} ---") 
    print(f"{words} were found in the document")
    print("")
    for i in char_list:
        print(f"The '{i['letter']}' character was found {i['value']} times")
    print("--- End report ---")

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    letters = {}
    for word in text:
        lower_letter = word.lower()
        if lower_letter in letters:
            letters[lower_letter] += 1
        else:
            letters[lower_letter] = 1
    return letters

def sort_on(dict):
    return dict["value"]

def char_layout(raw_chars):
    list = []
    
    for char in raw_chars:
        if char.isalpha():
            char_dict = {}
            char_dict['letter'] = char
            char_dict['value'] = raw_chars[char]
            list.append(char_dict)

    list.sort(reverse=True, key=sort_on)

    return list


main()