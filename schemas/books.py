from sqlalchemy import Column, String, DATE, MetaData, Table, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.ext.declarative import declarative_base

# from .users import User

Base = declarative_base()
# metadata = MetaData()

# books_table = Table(
#     "books",
#     metadata,
#     Column("book_id", UUID(as_uuid=True), primary_key=True),
#     Column("name", String(30), nullable=False),
#     Column("author_id", ForeignKey(users_table.c.user_id), nullable=False),
#     Column("create_date", DATE(), nullable=False),
#     Column("last_change_date", DATE()),
#     Column("publish_date", DATE()),
# )

class Book(Base):
    __tablename__ = 'books'
    metadata = MetaData()

    book_id: Column[UUID] = Column("book_id", UUID(as_uuid=True), primary_key=True)
    name: Column[String] = Column("name", String(30), nullable=False)
    author_id: Column[UUID] = Column("author_id", ForeignKey('users.user_id'), nullable=False)
    create_date: Column[DATE] = Column("create_date", DATE(), nullable=False)
    last_change_date: Column[DATE] = Column("last_change_date", DATE())
    publish_date: Column[DATE] = Column("publish_date", DATE())
    # authors = relationship(User)

# mapper(Book, books_table)