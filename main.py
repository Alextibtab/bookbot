class Book:
    path = "books/"

    def __init__(self, title):
        self.__title = title
        self.__contents = []
        with open(Book.path + title) as book:
            self.__contents = book.read()


    def get_title(self):
        return self.__title


    def get_word_count(self):
        return len(self.__contents.split())


    def letter_frequency(self):
        letter_count = {}
        for word in self.__contents:
            for letter in word:
                letter = letter.lower()
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        return letter_count


    def book_report(self):
        print(f"--- Begin report {Book.path+self.__title} ---")
        print(f"{self.get_word_count()} words found in this document\n")
        freq = self.letter_frequency()
        freq_sorted = {key: val for key, val in sorted(freq.items(), key = lambda ele: ele[1], reverse = True) if key.isalpha()}
        for letter, count in freq_sorted.items():
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")

if __name__ == "__main__":
    frankenstein = Book("frankenstein.txt")
    print(frankenstein.get_word_count())
    print(frankenstein.letter_frequency())
    frankenstein.book_report()