import os
from fastapi import APIRouter, HTTPException, Path
from typing import Dict, Any, List, Annotated
from dotenv import load_dotenv

from src.app.repositories import OrderRepo, MenuRepo, OrderItemRepo
from src.app.schemas import OrderBaseSchema, MenuItemSchema, OrderItemSchema, OrdersSchema, MenuItemsSchema, OrderSchema
from src.app.services import CommonService

load_dotenv()

router = APIRouter()

pk_type = Annotated[int, Path(ge=1, lt=1_000_000)]


@router.get(path="/",
            response_model=OrdersSchema,
            tags=["Страница отображения списка заказов"],
            summary="Orders list",
            )
async def order_list() -> Dict[str, Any]:
    """
    Функция получения списка заказов.

    :возврат: html-страница списка заказов.
    """
    order_list = await CommonService(OrderRepo).get_all(OrdersSchema())
    print(f"order_list order_list: {order_list}")
    return order_list


@router.get(path="/new/",
            # response_model=AddressResponseSchema,
            tags=["Страница отображения списка заказов"],
            summary="order_create",
            )
async def order_create() -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """

    history_dict = {"message": "new order"}
    return history_dict


@router.post(path="/new/",
             response_model=OrderBaseSchema,
             tags=["Страница отображения списка заказов"],
             summary="order_create",
             )
async def order_create(request: OrderBaseSchema) -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """
    print(f"order_create request: {request}")
    order_id = await CommonService(OrderRepo).add_one(request)
    order_dict = await CommonService(OrderRepo).get_one(order_id)
    print(f"order_create order_dict: {order_dict}")
    return order_dict


@router.get(path="/revenue/",
            # response_model=AddressResponseSchema,
            tags=["Страница отображения списка заказов"],
            summary="revenue_report",
            )
async def revenue_report() -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """

    history_dict = {"message": "revenue_report"}
    return history_dict


@router.post(path="/items/{pk}/add/",
             response_model=OrderItemSchema,
             tags=["Страница отображения списка заказов"],
             summary="order_item_add",
             )
async def order_item_add(request: OrderItemSchema, pk: pk_type) -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """
    print(f"order_item_add pk: {pk}, request: {request}")
    request.order_id = pk
    print(f"order_item_add request: {request}")
    order_item_id = await CommonService(OrderItemRepo).add_one(request)
    order_item_dict = await CommonService(OrderItemRepo).get_one(order_item_id)
    print(f"order_item_add order_item_dict: {order_item_dict}")
    return order_item_dict


@router.post(path="/items/{pk}/delete/",
             # response_model=AddressResponseSchema,
             tags=["Страница отображения списка заказов"],
             summary="order_item_delete",
             )
async def order_item_delete(request, pk: pk_type) -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """

    history_dict = {"message": "order_item_delete"}
    return history_dict


@router.get(path="/menu-item/",
            response_model=MenuItemsSchema,
            tags=["Страница отображения списка заказов"],
            summary="menu_item_list",
            )
async def menu_item_list() -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """
    menu_item = await CommonService(MenuRepo).get_all(MenuItemsSchema())
    print(f"order_list menu_item: {menu_item}")
    return menu_item


@router.get(path="/menu-item/new/",
            # response_model=MenuItemSchema,
            tags=["Страница отображения списка заказов"],
            summary="menu_item_create",
            )
async def menu_item_create() -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """
    history_dict = {"message": "menu_item_create"}
    return history_dict


@router.post(path="/menu-item/new/",
             response_model=MenuItemSchema,
             tags=["Страница отображения списка заказов"],
             summary="menu_item_create",
             )
async def menu_item_create(request: MenuItemSchema) -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """

    print(f"menu_item_create request: {request}")
    menu_item_id = await CommonService(MenuRepo).add_one(request)
    menu_item_dict = await CommonService(MenuRepo).get_one(menu_item_id)
    print(f"menu_item_create menu_item_dict: {menu_item_dict}")
    return menu_item_dict


@router.get(path="/{pk}/",
            # response_model=AddressResponseSchema,
            tags=["Страница отображения списка заказов"],
            summary="order_detail",
            )
async def order_detail(pk: pk_type) -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """

    history_dict = {"message": "order_detail"}
    return history_dict


@router.get(path="/{pk}/edit/",
            # response_model=AddressResponseSchema,
            tags=["Страница отображения списка заказов"],
            summary="order_update",
            )
async def order_update(pk: pk_type) -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """

    history_dict = {"message": "order_update"}
    return history_dict


@router.get(path="/{pk}/edit/",
            # response_model=AddressResponseSchema,
            tags=["Страница отображения списка заказов"],
            summary="order_update",
            )
async def order_update(request, pk: pk_type) -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """

    history_dict = {"message": "order_update"}
    return history_dict


@router.get(path="/{pk}/delete/",
            # response_model=AddressResponseSchema,
            tags=["Страница отображения списка заказов"],
            summary="order_delete",
            )
async def order_delete(request, pk: pk_type) -> Dict[str, Any]:
    """
    Функция создания заказа.

    :возврат: html-страница списка заказов.
    """

    history_dict = {"message": "order_delete"}
    return history_dict
