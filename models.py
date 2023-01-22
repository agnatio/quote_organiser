from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    quote = Column(String)
    book_reference = Column(String)
    categories = relationship('Category', secondary='quote_category', back_populates='quotes')

    def __repr__(self):
        return f"Quote: {self.quote} - Book: {self.book_reference}, Categories: {self.categories.__repr__()}"

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    quotes = relationship('Quote', secondary='quote_category', back_populates='categories')

    def __repr__(self):
        return f"Category: {self.name}"

class QuoteCategory(Base):
    __tablename__ = 'quote_category'
    quote_id = Column(Integer, ForeignKey('quotes.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), primary_key=True)


