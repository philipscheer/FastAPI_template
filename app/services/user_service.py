from sqlalchemy.orm import Session
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, User
from app.exceptions import UserNotFoundError, DatabaseError

class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, db: Session, user: UserCreate) -> User:
        try:
            return self.user_repository.create_user(db, user)
        except Exception as e:
            raise DatabaseError(str(e))

    def get_user(self, db: Session, user_id: int) -> User:
        try:
            user = self.user_repository.get_user(db, user_id)
            if not user:
                raise UserNotFoundError(user_id)
            return user
        except Exception as e:
            raise DatabaseError(str(e))
