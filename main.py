import sys

from stats import get_word_count

class Book:
    def __init__(self, path):
        self.__title = path.split("/")[-1]
        self.__contents = []
        with open(path) as book:
            self.__contents = book.read()


    def get_title(self):
        return self.__title


    def get_contents(self):
        return self.__contents


    def letter_frequency(self):
        letter_count = {}
        for word in self.get_contents():
            for letter in word:
                letter = letter.lower()
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        return letter_count


    def book_report(self):
        print(f"--- Begin report {self.get_title()} ---")
        print(f"{get_word_count(self.get_contents())} words found in the document\n")
        freq = self.letter_frequency()
        freq_sorted = {key: val for key, val in sorted(freq.items(), key = lambda ele: ele[1], reverse = True) if key.isalpha()}
        for letter, count in freq_sorted.items():
            print(f"{letter}: {count}")
        print("--- End report ---")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = Book(sys.argv[1])
    book.book_report()
