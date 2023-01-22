from controller import QuoteController

class QuoteView:
    def __init__(self):
        self.controller = QuoteController()

    def create_tables(self):
        self.controller.create_tables()

    def insert_quote(self, quote, book_reference):
        try:
            self.controller.insert_quote(quote, book_reference)
        except Exception as e:
            print(e)

    def insert_category(self, name):
        try:
            self.controller.insert_category(name)
        except Exception as e:
            print(e)

    def assign_category(self, category_name, quote_id):
        try:
            self.controller.assign_category(category_name, quote_id)
        except Exception as e:
            print(e)

if __name__ == '__main__':

    # Create tables
    quote_view = QuoteView()
    quote_view.create_tables()

    # Add categories
    try:
        quote_view.insert_category("optimistic")
    except Exception as e:
        print(e)
    try:
        quote_view.insert_category("pessimistic")
    except Exception as e:
        print(e)

    # Insert quotes
    quote_view.insert_quote("The sun is shining", "1984")
    quote_view.insert_quote("It's a rainy day", "1984")

    # Assign categories to quotes
    quote_view.assign_category("optimistic", 1)
    quote_view.assign_category("pessimistic", 2)

