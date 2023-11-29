import json
from fastapi import Body
from pydantic import BaseModel, Field, SecretStr, field_serializer
from typing_extensions import Annotated
from uuid import UUID, uuid1
from datetime import datetime, date

class UserLogin(BaseModel):
    login: str = Field(title='Login for authentication', max_length=20)
    hashed_password: SecretStr = Field(title='Password', max_length=50)

class UserSingUp(UserLogin):
    first_name: str = Field(title='First name or pseudonym', max_length=50)
    last_name: str = Field(title='Last name or pseudonym', max_length=50)
    email: str | None = Field(default=None, title="User email address", max_length=50, min_length=5)
    phone_number: str | None = Field(default=None, title='User phonenumber', max_length=10)

    @field_serializer('hashed_password', when_used='json')
    def dump_secret(self, v):
        return v.get_secret_value()

# class User1(UserSingUp):
#     user_id: UUID = Field(default=uuid1())
#     login_date: Annotated[date, Body()] = Field(default=datetime.now().date())

#     def __init__(self, user_sign_up: UserSingUp):
#         data = json.loads(user_sign_up.model_dump_json())
#         super().__init__(**data)

#     class Config:
#         from_attributes = True

class User(BaseModel):
    user_id: UUID = Field(default=uuid1())
    login: str = Field(title='Login for authentication', max_length=20)
    first_name: str = Field(title='First name or pseudonym', max_length=50)
    last_name: str = Field(title='Last name or pseudonym', max_length=50)
    email: str | None = Field(default=None, title="User email address", max_length=50, min_length=5)
    phone_number: str | None = Field(default=None, title='User phonenumber', max_length=10)
    login_date: Annotated[date, Body()] = Field(default=datetime.now().date())
    hashed_password: str

    def __init__(self, user_sign_up: UserSingUp):
        data = json.loads(user_sign_up.model_dump_json())
        super().__init__(**data)

    class Config:
        from_attributes = True

class BookChanges(BaseModel):
    book_id: UUID
    last_change_date: Annotated[datetime | None, Body()]

class Book(BookChanges):
    name: str = Field(default='Unnamed', title='Books name', max_length=50, serialization_alias='book_name')
    author_id: UUID
    publish_date: Annotated[date | None, Body()] = Field(default=None, title='Date of books publish (if None - no publish yet)')

    class Config:
        from_attributes = True
