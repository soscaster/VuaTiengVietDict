# utf-8 encoding support
import sys
import io
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
clear = lambda: os.system('clear')

# Search for a word in the dictionary
def search_word(word):
    with open('vv30K.txt', 'r', encoding='utf-8') as file:
        for line in file:
            if line.startswith('@' + word):
                # Print the word
                print(f"Đã tìm được từ: {word}")
                # Print the definition
                print("-----------------------------")
                print(f"Định nghĩa của từ: {word}")
                definition = line.strip()[len(word)+1:]
                while True:
                    next_line = next(file).strip()
                    if not next_line.startswith('-'):
                        break
                    definition += '\n' + next_line[1:]
                return definition
    return f"Xin lỗi, từ '{word}' không có trong dữ liệu từ điển."

clear()
word = input("Hãy nhập từ mà bạn cần tra cứu: ")
print("-----------------------------")
print("Đang tìm kiếm...")
print("-----------------------------")
print(search_word(word))