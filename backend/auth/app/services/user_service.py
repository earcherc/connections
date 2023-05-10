from fastapi import HTTPException, Depends
from app.models import User as UserTable
from pydantic import BaseModel
from passlib.context import CryptContext
from sqlmodel import Session
from typing import Optional
from app.database import get_session

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class User(BaseModel):
    username: str
    email: str
    password: Optional[str] = None


class UserInDB(User):
    hashed_password: str


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(
    username: str, session: Session = Depends(get_session)
) -> Optional[UserInDB]:
    user = session.get(UserTable, username)
    if user:
        return UserInDB(
            username=user.username, email=user.email, hashed_password=user.password
        )


async def register_user(user_data: User, session: Session):
    # Check if the username or email already exists in the database
    existing_user = session.get(UserTable, user_data.username) or session.get(
        UserTable, user_data.email
    )
    if existing_user:
        raise HTTPException(status_code=400, detail="Username or email already exists")

    # Hash the user's password
    hashed_password = get_password_hash(user_data.password)

    # Create a new user with the hashed password
    new_user = UserTable(
        username=user_data.username, email=user_data.email, password=hashed_password
    )

    # Add the new user to the session
    session.add(new_user)

    # Commit the transaction
    session.commit()

    # Refresh the user object to get the ID assigned by the database
    session.refresh(new_user)

    return new_user.id
