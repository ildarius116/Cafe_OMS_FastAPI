from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class MenuItemSchema(BaseModel):
    name: str
    price: Optional[float]

    class Config:
        from_attributes = True


class MenuItemsSchema(BaseModel):
    menu_items: Optional[List[MenuItemSchema]] = None


class OrderItemSchema(BaseModel):
    order: int
    menu_item: int
    quantity: Optional[int]
    price: Optional[float]

    class Config:
        from_attributes = True


class OrderSchema(BaseModel):
    id: int
    table_number: int = Field(ge=1, le=100, description="Номер стола")
    order_items: Optional[List[OrderItemSchema]] = None
    total_price: Optional[float] = Field(0, ge=0, description="Общая стоимость")
    status: str = Field(default="pending")
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class OrdersSchema(BaseModel):
    orders: Optional[List[OrderSchema]] = None
