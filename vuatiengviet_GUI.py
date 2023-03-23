# -*- coding: utf-8 -*-

#                            _
#                         _ooOoo_
#                        o8888888o
#                        88" . "88
#                        (| -_- |)
#                        O\  =  /O
#                     ____/`---'\____
#                   .'  \\|     |//  `.
#                  /  \\|||  :  |||//  \
#                 /  _||||| -:- |||||_  \
#                 |   | \\\  -  /'| |   |
#                 | \_|  `\`---'//  |_/ |
#                 \  .-\__ `-. -'__/-.  /
#               ___`. .'  /--.--\  `. .'___
#            ."" '<  `.___\_<|>_/___.' _> \"".
#           | | :  `- \`. ;`. _/; .'/ /  .' ; |
#           \  \ `-.   \_\_`. _.'_/_/  -' _.' /
# ===========`-.`___`-.__\ \___  /__.-'_.'_.-'================
# THIEN TAI - THIEN TAI   `=--=-'        THIEN TAI - THIEN TAI
#        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#              Phật phù hộ, không bao giờ BUG
#        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import tkinter as tk
import os
import sys

# UTF-8 encoding for Vietnamese characters
os.environ['PYTHONIOENCODING'] = 'utf-8'

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class Word:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition

class DictionaryGUI:
    def __init__(self):
        self.dictionary = self.load_dictionary()
        self.create_gui()

    def load_dictionary(self):
        dictionary = {}
        with open('data/vv30K.txt', 'r', encoding='utf-8') as file:
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
            self.definition_label.config(text=self.dictionary[word].definition)
        else:
            self.definition_label.config(text="Xin lỗi, từ này không có trong dữ liệu từ điển.")

    def on_word_selected(self, event):
        word = self.index_listbox.get(tk.ACTIVE)
        self.search_word(word)

    def on_search_word(self, event=None):
        word = self.search_entry.get()
        self.search_word(word)

    def create_gui(self):
        root = tk.Tk()
        root.title("Từ điển Vua Tiếng Việt - CG Version")

        # Create widgets
        self.index_listbox = tk.Listbox(root)
        self.definition_label = tk.Label(root, wraplength=620)
        self.search_entry = tk.Entry(root)
        search_button = tk.Button(root, text="Tìm kiếm")
        copy_word_button = tk.Button(root, text="Sao chép từ")
        copy_definition_button = tk.Button(root, text="Sao chép định nghĩa")

        # Populate index listbox
        for word in self.dictionary:
            self.index_listbox.insert(tk.END, word)

        # Scrollbar
        scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=self.index_listbox.yview)
        self.index_listbox.config(yscrollcommand=scrollbar.set)

        # Bind events
        self.index_listbox.bind('<ButtonRelease-1>', self.on_word_selected)
        self.search_entry.bind('<Return>', self.on_search_word)
        search_button.config(command=self.on_search_word)
        copy_word_button.config(command=lambda: root.clipboard_clear() or root.clipboard_append(self.index_listbox.get(tk.ACTIVE)))
        copy_definition_button.config(command=lambda: root.clipboard_clear() or root.clipboard_append(self.definition_label.cget('text')))

        # Layout widgets
        self.index_listbox.grid(row=0, column=0, rowspan=2, sticky='NS')
        scrollbar.grid(row=0, column=1, rowspan=2, sticky='NS')
        self.definition_label.grid(row=0, column=2, rowspan=3, columnspan=4, sticky='NSEW', padx=10, pady=10)
        self.search_entry.grid(row=1, column=2, sticky='EW', padx=5, pady=10)
        search_button.grid(row=1, column=3, padx=5, pady=10)
        copy_word_button.grid(row=1, column=4, padx=5, pady=10)
        copy_definition_button.grid(row=1, column=5, padx=5, pady=10)
                
        # Set window properties
        root.geometry('800x600')
        root.rowconfigure(0, weight=1)
        root.columnconfigure(2, weight=1)

        # Print first start up message
        # Set font style, size and alignment
        self.definition_label.config(font=('Arial', 14), justify='center')
        # Create more space between lines
        self.definition_label.config(anchor='n')
        # Set text
        self.definition_label.config(text="Chào mừng bạn đến với Từ điển Vua Tiếng Việt - CG Version!\n\nHãy chọn (double click) từ bạn cần tra cứu từ danh sách bên trái.\n\nNếu không tìm thấy từ bạn cần, hãy nhập từ vào ô bên dưới và nhấn nút 'Tìm kiếm'.\n\nNếu bạn muốn sao chép từ hoặc định nghĩa, hãy nhấn nút 'Sao chép từ' hoặc 'Sao chép định nghĩa'.\n\nChúc bạn có một ngày tốt lành!\n\n\n\n\n\nEmail: main@quangminh.name.vn\nWebsite: https://landing.quangminh.name.vn\nFacebook: https://facebook.com/v7.minh\n\n© 2023 - Nguyễn Quang Minh. All rights reserved.")

        # Start GUI loop
        root.mainloop()

if __name__ == '__main__':
    DictionaryGUI()

# pyinstaller -F --clean -y -n "vuatiengviet" --add-data="vv30K.txt:." vuatiengviet_GUI.py