from sqlalchemy import Column, String, DATE, MetaData, Table
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import mapper, relationship
from sqlalchemy.ext.declarative import declarative_base

from .books import Book

Base = declarative_base()
# metadata = MetaData()

# users_table = Table(
#     "users",
#     metadata,
#     Column("user_id", UUID(as_uuid=True), primary_key=True),
#     Column("login", String(30), nullable=False, unique=True),
#     Column("first_name", String(50), nullable=False),
#     Column("last_name", String(50), nullable=False),
#     Column("email", String(50), nullable=False, unique=True),
#     Column("phone_number", String(10)),
#     Column("login_date", DATE(), nullable=False),
#     Column("hashed_password", String(50)),
# )

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
    books = relationship(Book)

# mapper(User, users_table)