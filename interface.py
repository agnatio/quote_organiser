import tkinter as tk
from tkinter import ttk
from view import QuoteView

class QuoteViewWithCategory:
    def __init__(self):
        self.view = QuoteView()
        self.root = tk.Tk()
        self.create_widgets()

    def create_widgets(self):
        self.quotes_listbox = tk.Listbox(self.root)
        self.quotes_listbox.pack()

        quotes = self.view.controller.get_all_quotes()
        for quote in quotes:
            categories = ', '.join([category.name for category in quote.categories])
            self.quotes_listbox.insert(tk.END, f"{quote.quote} - {categories}")

    def run(self):
        self.root.mainloop()

if __name__ == '__main__':
    quote_view = QuoteViewWithCategory()
    quote_view.run()


# class QuoteInterface:
#     def __init__(self):
#         self.view = QuoteView()
#         self.root = tk.Tk()
#         self.create_widgets()

#     def create_widgets(self):

#         self.insert_quote_label = ttk.Label(self.root, text="Insert Quote")
#         self.insert_quote_label.pack()

#         self.quote_entry = ttk.Entry(self.root)
#         self.quote_entry.pack()

#         self.author_entry = ttk.Entry(self.root)
#         self.author_entry.pack()

#         self.insert_quote_button = ttk.Button(self.root, text="Insert quote", command=self.insert_quote)
#         self.insert_quote_button.pack()

#     def create_tables(self):
#         self.view.create_tables()

#     def insert_quote(self):
#         quote = self.quote_entry.get()
#         self.view.insert_quote(quote)

#     def run(self):
#         self.root.mainloop()

# if __name__ == '__main__':
#     interface = QuoteInterface()
#     interface.run()