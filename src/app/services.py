from typing import Union

from src.app.schemas import MenuItemSchema, OrderItemSchema, OrderBaseSchema, OrdersSchema, MenuItemsSchema, OrderSchema
from src.utils.repository import AbstractRepository


class CommonService:
    def __init__(self, common_repository: AbstractRepository):
        self.common_repository: AbstractRepository = common_repository()

    async def add_one(self, common_schemas: Union[OrderSchema, OrderItemSchema, MenuItemSchema]) -> int:
        common_dict = common_schemas.model_dump()
        print(f"CommonService add_one common_dict: {common_dict}")
        common_id = await self.common_repository.add_one(common_dict)
        print(f"CommonService add_one common_id: {common_id}")
        return common_id

    async def get_one(self, common_id: int):
        print(f"OrderService get_one order_id: {common_id}")
        common_dict = await self.common_repository.get_one(common_id)
        print(f"OrderService get_one common_dict: {common_dict}")
        return common_dict

    async def get_all(self, common_schemas: Union[OrdersSchema, OrderItemSchema, MenuItemsSchema]):
        common_dict = common_schemas.model_dump()
        common_list = await self.common_repository.get_all(**common_dict)
        common_schemas.lists = common_list
        return common_schemas
