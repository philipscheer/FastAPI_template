from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from app.core.security import hash_password

class UserRepository:
    def create_user(self, db: Session, user: UserCreate) -> User:
        try:
            # Converter password para hashed_password
            user_data = user.dict()
            user_data["hashed_password"] = hash_password(user_data.pop("password"))
            db_user = User(**user_data)
            db.add(db_user)
            db.commit()
            db.refresh(db_user)
            return db_user
        except Exception as e:
            db.rollback()
            raise Exception(f"Erro ao criar usuario: {str(e)}")

    def get_user(self, db: Session, user_id: int) -> User:
        try:
            return db.query(User).filter(User.id == user_id).first()
        except Exception as e:
            raise Exception(f"Erro ao buscar usuario: {str(e)}")
