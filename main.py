def count_char(string_in):
    string_in_lowered = string_in.lower()
    chars = {}
    for char in string_in_lowered:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars
    

#Main function, opens book, counts words, prints word count first
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        char_dictionary = count_char(file_contents)
        print(f"Total Word Count: {word_count}")
        print(char_dictionary)

main()