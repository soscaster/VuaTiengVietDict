# utf-8 encoding support
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition


class Main:
    def __init__(self):
        self.clear()
        self.dictionary = self.load_dictionary()
        self.run()

    def clear(self):
        os.system('clear')

    def load_dictionary(self):
        dictionary = {}
        with open('vv30K.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if line.startswith('@'):
                    word = line.strip()[1:]
                    definition = ''
                    try:
                        next_line = next(file).strip()
                        while next_line.startswith('-'):
                            definition += '\n' + next_line[1:]
                            next_line = next(file).strip()
                        dictionary[word] = Word(word, definition)
                    except StopIteration:
                        dictionary[word] = Word(word, definition)
        return dictionary

    def search_word(self, word):
        if word in self.dictionary:
            print(f"Đã tìm được từ: {word}")
            print("-----------------------------")
            print(f"Định nghĩa của từ '{word}':")
            return self.dictionary[word].definition
        else:
            print(f"Xin lỗi, từ '{word}' không có trong dữ liệu từ điển.")
            print("-----------------------------")

    def run(self):
        while True:
            self.clear()
            word = input("Hãy nhập từ mà bạn cần tra cứu (nhập 'q' hoặc 'quit' để thoát chương trình): ")
            if word == 'quit' or word == 'q':
                break
            print("-----------------------------")
            print("Đang tìm kiếm...")
            print("-----------------------------")
            print(self.search_word(word))
            print("-----------------------------")
            input("Nhấn Enter để tiếp tục...")

if __name__ == '__main__':
    Main()
