from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.utils.repository import SQLAlchemyRepository
from src.app.models import MenuItemModel, OrderItemModel, OrderModel


class OrderRepo(SQLAlchemyRepository):
    model = OrderModel

    async def get_one(self, target_id: int):
        query = select(self.model).options(
            selectinload(self.model.order_items)
            .selectinload(OrderItemModel.menu_item)
        ).where(self.model.id == target_id)
        return await super().get_one(query)


class OrderItemRepo(SQLAlchemyRepository):
    model = OrderItemModel

    async def get_one(self, target_id: int):
        query = select(self.model).where(self.model.id == target_id)
        return await super().get_one(query)


class MenuRepo(SQLAlchemyRepository):
    model = MenuItemModel

    async def get_one(self, target_id: int):
        query = select(self.model).where(self.model.id == target_id)
        return await super().get_one(query)
