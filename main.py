def main():
    book_path = "./books/frankenstein.txt"
    content = read_file(book_path)
    letters = count_letters(content)
    print(print_report(letters))


def read_file(path):
    with open(path) as file:
        return file.read()


def get_words_count(content):
    return len(content.split())


def count_letters(content):
    words = content.lower().split()
    letters = dict()

    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters


def print_report(letters):
    for letter in letters:
        print(f"The '{letter}' character ws found {letters[letter]} times")


main()
