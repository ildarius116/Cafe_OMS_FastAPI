from abc import ABC, abstractmethod

from sqlalchemy import select, insert
from src.database import async_session


class AbstractRepository(ABC):
    model = None

    @abstractmethod
    async def add_one(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def get_one(self, *args, **kwargs):
        raise NotImplemented

    @abstractmethod
    async def get_all(self, *args, **kwargs):
        raise NotImplemented


class SQLAlchemyRepository(AbstractRepository):
    model = None

    async def init_one(self, data: dict) -> int:
        print(f"SQLAlchemyRepository init_one data: {data}")
        async with async_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            print(f"SQLAlchemyRepository init_one stmt: {stmt}")
            result = await session.execute(stmt)
            print(f"SQLAlchemyRepository init_one session: {session}")
            await session.flush()
            await session.commit()
            return result.scalar_one()

    async def add_one(self, data: dict) -> int:
        print(f"SQLAlchemyRepository add_one data: {data}")
        data = {k: v for k, v in data.items() if v is not None}
        async with async_session() as session:
            stmt = insert(self.model).values(**data).returning(self.model.id)
            print(f"SQLAlchemyRepository add_one stmt: {stmt}")
            result = await session.execute(stmt)
            print(f"SQLAlchemyRepository add_one session: {session}")
            await session.commit()
            return result.scalar_one()

    async def get_one(self, target_id):
        async with async_session() as session:
            query = select(self.model).where(self.model.id == target_id)
            result = await session.execute(query)
            # log = result.all()[0][0].to_read_model()
            # return log
            instance = result.scalar_one()
            return instance
            # await session.refresh(instance, ['order_items'])
            # return instance.to_read_model()

    async def get_all(self, **kwargs):
        async with async_session() as session:
            query = (select(self.model)
                     # .order_by(self.model.timestamp.desc())
                     )
            res = await session.execute(query)
            res = [row[0].to_read_model() for row in res.all()]
            return res
