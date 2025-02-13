def count_words(string): 
    return len(string.split())

def get_text_from_file(file_path):
    with open(file_path) as f:
        return f.read()

def get_word_count(text):
    return len(text.split())

def get_symbol_data(text):
    lowered_text = text.lower()
    char_data = {}

    for char in lowered_text:
        if char in char_data:
            char_data[char] += 1
        else:
            char_data[char] = 1

    return  char_data

def format_char_data(char_data):
    formatted_char_data_list = []
    for key in char_data:
        if key in "abcdefghijklmnopqrstuvwxyz":
            formatted_char_data_list.append({ "name": key, "num": char_data[key]})
    return formatted_char_data_list

def sort_on(dict):
    return dict["num"]

def show_char_report(file_path):
    text = get_text_from_file(file_path) 
    word_count = get_word_count(text)
    char_data = get_symbol_data(text)
    formatted_char_data_list = format_char_data(char_data)
    formatted_char_data_list.sort(reverse=True, key=sort_on)

    print(f"--- Begin report of {file_path} ---")
    print(f"{word_count} words found in the document")
    for formatted_char_data in formatted_char_data_list:
        char = formatted_char_data["name"]
        num = formatted_char_data["num"]
        print(f"The '{char}' character was found {num} times")

    print(f"--- End report ---")

def main():
    file_path = "books/frankenstein.txt"
    show_char_report(file_path)

main()