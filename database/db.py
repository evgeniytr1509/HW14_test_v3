from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


import contextlib
from typing import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase



SQLALCHEMY_DATABASE_URL = "postgresql://postgres:567234@195.201.150.230:5433/evgeniy_rt_fa" #
engine = create_engine(SQLALCHEMY_DATABASE_URL)


# class DatabaseSessionManager:
#     def __init__(self, url: str):
#         self._engine: AsyncEngine | None = create_async_engine(url)
#         self._session_maker: async_sessionmaker | None = async_sessionmaker(autocommit=False,
#                                                                             autoflush=False,
#                                                                             expire_on_commit=False,
#                                                                             bind=self._engine)


#     @contextlib.asynccontextmanager
#     async def session(self) -> AsyncIterator[AsyncSession]:
#         if self._session_maker is None:
#             raise Exception("DatabaseSessionManager is not initialized")
#         session = self._session_maker()
#         try:
#             yield session
#         except Exception as err:
#             print(err)
#             await session.rollback()
#         finally:
#             await session.close()


# # Dependency
# async def get_db():
#     async with sessionmanager.session() as session:
#         yield session



# Определение Base
Base = declarative_base()



# Функция для получения сессии базы данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




