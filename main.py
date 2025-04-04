from stats import word_counter
import sys
#Counts characters, skipping non-alpha characters like spaces, periods, commas, etc.
def count_char(string_in):
    string_in_lowered = string_in.lower()
    chars = {}
    for char in string_in_lowered:
        if char in chars and char.isalpha() == True:
            chars[char] += 1
        elif char not in chars and char.isalpha() == True:
            chars[char] = 1
    return chars
#Converts the count_char dict into a list of dictionaries for further iteration, sorting, and output
def dict_conversion(char_dictionary):
    char_dict_list = []
    for char, count in char_dictionary.items():
        new_dict = {"char": char, "num": count}
        char_dict_list.append(new_dict)
    return char_dict_list
#Sorts the list of dictionaries created above
def sort_on(char_dict_list):
    return char_dict_list["num"]    

#Main function, opens book, counts words, prints word count first
def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        word_count = word_counter(file_contents)
        char_dictionary = count_char(file_contents)
        char_dict_list = dict_conversion(char_dictionary)
        char_dict_list.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\nThe following is a list of each alphabetical letter used in the document, with capital letters converted to lower case.")
        for item in char_dict_list:
            print(f"{item['char']}: {item['num']}")
        print("--- End report ---")
main()