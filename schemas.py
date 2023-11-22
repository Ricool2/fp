from sqlalchemy import Column, String, DATE, MetaData, Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    metadata = MetaData()

    user_id: Column[UUID] = Column("user_id", UUID(as_uuid=True), primary_key=True)
    login: Column[String] = Column("login", String(30), nullable=False, unique=True)
    first_name: Column[String] = Column("first_name", String(50), nullable=False)
    last_name: Column[String] = Column("last_name", String(50), nullable=False)
    email: Column[String] = Column("email", String(50), nullable=False, unique=True)
    phone_number: Column[String] = Column("phone_number", String(10))
    login_date: Column[DATE] = Column("login_date", DATE(), nullable=False)
    hashed_password: Column[String] = Column("hashed_password", String(50))
    _books = relationship("Book", backref="user")

class Book(Base):
    __tablename__ = 'books'
    metadata = MetaData()

    book_id: Column[UUID] = Column("book_id", UUID(as_uuid=True), primary_key=True)
    name: Column[String] = Column("name", String(30), nullable=False)
    author_id: Column[UUID] = Column("author_id", ForeignKey(User.user_id), nullable=False)
    create_date: Column[DATE] = Column("create_date", DATE(), nullable=False)
    last_change_date: Column[DATE] = Column("last_change_date", DATE())
    publish_date: Column[DATE] = Column("publish_date", DATE())
    # authors = relationship('User', back_populates ="books")