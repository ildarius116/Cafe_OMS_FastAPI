from src.utils.repository import SQLAlchemyRepository
from src.app.models import MenuItemModel, OrderItemModel, OrderModel


class OrderRepo(SQLAlchemyRepository):
    model = OrderModel


class OrderItemRepo(SQLAlchemyRepository):
    model = OrderItemModel


class MenuRepo(SQLAlchemyRepository):
    model = MenuItemModel
