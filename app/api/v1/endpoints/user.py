from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import User, UserCreate
from app.services.user_service import UserService
from app.repositories.user_repository import UserRepository
from app.db.session import SessionLocal
from app.exceptions import UserNotFoundError, DatabaseError

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        user_repository = UserRepository()
        user_service = UserService(user_repository=user_repository)
        return user_service.create_user(db, user)
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    try:
        user_repository = UserRepository()
        user_service = UserService(user_repository=user_repository)
        db_user = user_service.get_user(db, user_id)
        if db_user is None:
            raise UserNotFoundError(user_id)
        return db_user
    except UserNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except DatabaseError as e:
        raise HTTPException(status_code=500, detail=str(e))
