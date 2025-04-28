from src.app.schemas import MenuItemSchema, OrderItemSchema, OrderSchema, OrdersSchema, MenuItemsSchema
from src.utils.repository import AbstractRepository


class OrderService:
    def __init__(self, order_repository: AbstractRepository):
        self.order_repository: AbstractRepository = order_repository()

    async def add_one(self, order: OrderSchema) -> int:
        order_dict = order.model_dump()
        print(f"OrderService add_one order_dict: {order_dict}")
        order_id = await self.order_repository.add_one(order_dict)
        print(f"OrderService add_one order_id: {order_id}")
        return order_id

    async def get_one(self, order_id: int):
        print(f"OrderService get_one order_id: {order_id}")
        order_dict = await self.order_repository.get_one(order_id)
        print(f"OrderService get_one order_dict: {order_dict}")
        return order_dict

    async def get_all(self, order: OrdersSchema):
        order_dict = order.model_dump()
        order_list = await self.order_repository.get_all(**order_dict)
        order.orders = order_list
        return order


class OrderItemService:
    def __init__(self, order_repository: AbstractRepository):
        self.order_repository: AbstractRepository = order_repository()

    async def add_one(self, order: OrderItemSchema, pk: int = None) -> int:
        order_dict = order.model_dump()
        print(f"OrderItemService add_one order_item_dict: {order_dict}")
        if pk:
            order_dict["order"] = pk
        print(f"OrderItemService add_one order_item_dict: {order_dict}")
        order_id = await self.order_repository.add_one(order_dict)
        print(f"OrderItemService add_one order_item_id: {order_id}")
        return order_id

    async def get_one(self, order_id: int):
        order_dict = await self.order_repository.get_one(order_id)
        return order_dict

    async def get_all(self, order: OrderItemSchema):
        order_dict = order.model_dump()
        order_list = await self.order_repository.get_all(**order_dict)
        order.logs = order_list
        return order


class MenuService:
    def __init__(self, menu_repository: AbstractRepository):
        self.menu_repository: AbstractRepository = menu_repository()

    async def add_one(self, menu_item: MenuItemSchema) -> int:
        menu_dict = menu_item.model_dump()
        print(f"MenuService add_menu_item menu_item_dict: {menu_dict}")
        menu_item_id = await self.menu_repository.add_one(menu_dict)
        print(f"MenuService add_menu_item menu_item_id: {menu_item_id}")
        return menu_item_id

    async def get_one(self, menu_item_id: int):
        print(f"MenuService get_one menu_item_id: {menu_item_id}")
        menu_item_dict = await self.menu_repository.get_one(menu_item_id)
        print(f"MenuService get_one menu_item_dict: {menu_item_dict}")
        return menu_item_dict

    async def get_all(self, order: MenuItemsSchema):
        order_dict = order.model_dump()
        order_list = await self.menu_repository.get_all(**order_dict)
        order.menu_items = order_list
        return order
