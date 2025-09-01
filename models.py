from sqlalchemy import create_engine, Column, Integer, String, Float, Date, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = 'publisher'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    
    # Relationships
    books = relationship('Book', back_populates='publisher')

class Shop(Base):
    __tablename__ = 'shop'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    
    # Relationships
    stocks = relationship('Stock', back_populates='shop')

class Book(Base):
    __tablename__ = 'book'
    
    id = Column(Integer, primary_key=True)
    title = Column(String(200), nullable=False)
    id_publisher = Column(Integer, ForeignKey('publisher.id'), nullable=False)
    
    # Relationships
    publisher = relationship('Publisher', back_populates='books')
    stocks = relationship('Stock', back_populates='book')

class Stock(Base):
    __tablename__ = 'stock'
    
    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey('book.id'), nullable=False)
    id_shop = Column(Integer, ForeignKey('shop.id'), nullable=False)
    count = Column(Integer, nullable=False)
    
    # Relationships
    book = relationship('Book', back_populates='stocks')
    shop = relationship('Shop', back_populates='stocks')
    sales = relationship('Sale', back_populates='stock')

class Sale(Base):
    __tablename__ = 'sale'
    
    id = Column(Integer, primary_key=True)
    price = Column(Float, nullable=False)
    date_sale = Column(Date, nullable=False)
    id_stock = Column(Integer, ForeignKey('stock.id'), nullable=False)
    count = Column(Integer, nullable=False)
    
    # Relationships
    stock = relationship('Stock', back_populates='sales')

def create_tables(engine):
    """Создает все таблицы в базе данных"""
    Base.metadata.create_all(engine) 