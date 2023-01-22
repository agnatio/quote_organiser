from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Quote, Category, QuoteCategory, Base
import sqlite3

class QuoteController:
    def __init__(self):
        self.engine = create_engine('sqlite:///quotes.db', echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

    def insert_quote(self, quote, book_reference):
        new_quote = Quote(quote=quote, book_reference=book_reference)
        try:
            self.session.add(new_quote)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print("An error occurred while inserting the quote: ", e)

    def insert_category(self, name):
        new_category = Category(name=name)
        try:
            self.session.add(new_category)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print("An error occurred while inserting the category: ", e)
        else:
            print("Category successfully inserted")


    def assign_category(self, category_name, quote_id):
        category = self.session.query(Category).filter(Category.name == category_name).first()
        quote = self.session.query(Quote).filter(Quote.id == quote_id).first()
        try:
            quote.categories.append(category)
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            print("An error occurred while assigning the category: ", e)

    def get_all_quotes(self):
        return self.session.query(Quote).all()


if __name__ == '__main__':

    """
    get all the quotes
    """
    quote_controller = QuoteController()
    quotes = quote_controller.get_all_quotes()

    print(quotes)



    pass
    # QuoteController().insert_category("optimistic")
    # QuoteController().insert_category("pessimistic")
    
    # quote_controller = QuoteController()
    # quote_controller.insert_quote("The sun is shining", "1984")

    # quote_controller = QuoteController()
    # quote_controller.create_tables()
    # quote_controller.insert_quote("A quote")