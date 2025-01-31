def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = len(file_contents.split())
        print(file_contents)
        print(f"Total Word Count: {word_count}")
main()