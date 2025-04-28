import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict

from src.app.repositories import MenuRepo, OrderItemRepo, OrderRepo
from src.app.services import MenuService, OrderItemService, OrderService


@pytest.mark.asyncio
async def test_menu_service(clean_db, menu_test_data):
    """
    Тест создания записи в БД напрямую
    """

    # добавление данных в БД
    menu_item_id = await MenuService(MenuRepo).add_one(menu_test_data)
    assert menu_item_id is not None

    # запрос данных из БД
    result = await MenuService(MenuRepo).get_one(menu_item_id)

    # проверка
    assert result.name == "soup"
    assert result.price == 10.0
