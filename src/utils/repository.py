from abc import ABC, abstractmethod
from sqlalchemy import select, insert
from sqlalchemy.orm import selectinload

from src.app.models import OrderItemModel
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

    async def add_one(self, data: dict) -> int:
        print(f"SQLAlchemyRepository add_one data: {data}")
        data = {k: v for k, v in data.items() if v is not None}
        try:
            async with async_session() as session:
                stmt = insert(self.model).values(**data).returning(self.model.id)
                print(f"SQLAlchemyRepository add_one stmt: {stmt}")
                result = await session.execute(stmt)
                print(f"SQLAlchemyRepository add_one result: {result}")
                await session.commit()
                return result.scalar_one()
        except Exception as e:
            print(f"Error in get_one: {e}")
            raise

    async def get_one(self, query):
        try:
            async with async_session() as session:
                print(f"SQLAlchemyRepository get_one query: {query}")
                result = await session.execute(query)
                instance = result.unique().scalar_one()
                print(f"SQLAlchemyRepository get_one instance: {instance}")
                return instance.to_read_model()
        except Exception as e:
            print(f"Error in get_one: {e}")
            raise

    async def get_all(self, **kwargs):
        try:
            async with async_session() as session:
                query = select(self.model).options(
                    selectinload(self.model.order_items).selectinload(OrderItemModel.menu_item)
                )
                print(f"SQLAlchemyRepository get_all query: {query}")
                res = await session.execute(query)
                print(f"SQLAlchemyRepository get_all res: {res}")
                res = [row[0].to_read_model() for row in res.all()]
                print(f"SQLAlchemyRepository get_all res: {res}")
                return res
        except Exception as e:
            print(f"Error in get_one: {e}")
            raise
