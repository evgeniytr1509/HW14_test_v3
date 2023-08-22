import logging

from libgravatar import Gravatar
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User
from schemas import UserSchema


async def get_user_by_email(email: str, db: AsyncSession) -> User:
    sq = select(User).filter_by(email=email)
    result = db.execute(sq)
    user = result.scalar_one_or_none()
    logging.info(user)
    return user

async def create_user(body: UserSchema, db: AsyncSession) -> User:
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        logging.error(e)
    new_user = User(**body.model_dump(), avatar=avatar)  # User(username=username, email=email, password=password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: AsyncSession) -> None:
    user.refresh_token = token
    db.commit()

async def confirmed_email(email: str, db: AsyncSession) -> None:
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()


async def main():
    async with AsyncSession() as session:
        email = "example@example.com"
        user = await get_user_by_email(email, session)
        if user:
            await update_token(user, "new_token", session)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())