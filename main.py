#project_env/Scripts/activate
from uuid import UUID
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from models import UserLogin, User, Book, BookChanges, UserSingUp
from schemas import User as UserShema, Book as BookShema
from typing import Union
import os
import uvicorn

app = FastAPI()

date_formats = {
    '-': '%d-%m-%Y',
    '.': '%d.%m.%Y',
    
    'r-': '%Y-%m-%d',
    'r.': '%Y.%m.%d',
}

engine = create_engine(os.environ.get('DATABASE_URL', 'postgresql+psycopg2://postgres:1134@127.0.0.1:5432/fp_base'))
# engine.connect()

async def get_db():
    try:
        session = Session(bind=engine)
        yield session
    except:
        shutdown()
    finally:
        session.close()
    
async def shutdown():
    session = Session(bind=engine)
    session.close()

app.add_event_handler("startup", get_db)
app.add_event_handler("shutdown", shutdown)

@app.get('/')
def root():
    return {'message': 'root'}

@app.get('/users/{user_id}', response_model=User)
def get_user_by_id(user_id: UUID, db: Session = Depends(get_db)):
    result = db.query(UserShema).filter(UserShema.user_id == user_id).one()
    return User.model_validate(result, from_attributes=True)

@app.get('/books/{book_id}', response_model=Book)
def get_book_by_id(book_id: UUID, db: Session = Depends(get_db)):
    result = db.query(BookShema).filter(BookShema.book_id == book_id).one()
    return Book.model_validate(result, from_attributes=True)

@app.post('/sign_up', response_model=User)
async def signup_user(user_info: UserSingUp, db: Session = Depends(get_db)):
    new_user = User(user_info)
    db_new_user = UserShema(**new_user.model_dump())
    db.add(db_new_user)
    db.commit()
    db.refresh(db_new_user)
    return User.model_validate(db_new_user)

@app.post('/del_user')
async def del_user(user_id: UUID, db: Session = Depends(get_db)):
    user = db.query(UserShema).filter(UserShema.user_id == user_id).one()
    db.delete(user)
    db.commit()
    return {'message': f'deleted {user.user_id} from users'}

if __name__ == "__main__":
    uvicorn.run("main:app", port=80, log_level="info")