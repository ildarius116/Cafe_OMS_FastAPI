import pytest
from unittest.mock import patch
from fastapi.testclient import TestClient
from httpx import AsyncClient, ASGITransport
from sqlalchemy import delete
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Any, Dict

# from src.database import get_db_session
from src.main import app
from src.app.models import MenuItemModel, OrderItemModel, OrderModel


@pytest.fixture(scope="module")
def client():
    return TestClient(app)


@pytest.mark.asyncio
async def test_get_orders(test_db_session: AsyncSession, clean_db):
    """
    Тест корректности работы API и формат пагинированного ответа без указания пагинации
    """
    async with AsyncClient(transport=ASGITransport(app),
                           base_url="http://test",
                           ) as ac:
        response = await ac.get("/")
        assert response.status_code == 200
        # data = response.json()
