import os
import pytest_asyncio
from typing import Dict, Any
from dotenv import load_dotenv
from sqlalchemy import delete, NullPool
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine, create_async_engine, async_sessionmaker

from src.app.models import MenuItemModel, OrderItemModel, OrderModel
from src.database import Base

load_dotenv()
DB_NAME = os.getenv('DB_NAME', "test_cafe")
DATABASE_URL = f"sqlite+aiosqlite:///./{DB_NAME}.db"

engine: AsyncEngine = create_async_engine(
    url=DATABASE_URL,
    poolclass=NullPool,
    echo=True
)

async_session = async_sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    expire_on_commit=False,
    class_=AsyncSession
)


@pytest_asyncio.fixture(scope="module")
async def test_db():
    """
    Функция-фикстура инициализации и очистка тестовой БД
    """

    async with engine.begin() as conn:
        print('BEFORE CREATE !!!!!!!!!!!!!!!!!')
        await conn.run_sync(Base.metadata.create_all)
        print('AFTER CREATE !!!!!!!!!!!!!!!!!')
    yield
    async with engine.begin() as conn:
        print('BEFORE DROP !!!!!!!!!!!!!!!!!')
        await conn.run_sync(Base.metadata.drop_all)
        print('AFTER DROP !!!!!!!!!!!!!!!!!')


@pytest_asyncio.fixture
async def clean_db(test_db_session: AsyncSession):
    """
    Функция-фикстура очистки БД перед тестом
    """
    await test_db_session.execute(delete(MenuItemModel))
    await test_db_session.execute(delete(OrderItemModel))
    await test_db_session.execute(delete(OrderModel))
    await test_db_session.commit()
    yield


@pytest_asyncio.fixture
async def mock_account_data():
    """
    Функция-фикстура
    """
    mock_account_data: Dict[str, Any] = {
        "address": "full_fields_address",
        "balance": 1000.0,
        "bandwidth": {"available": 50.0},
        "energy": {"available": 20.0}
    }
    return mock_account_data


@pytest_asyncio.fixture
async def menu_test_data():
    """
    Функция-фикстура
    """
    menu_data = [
        MenuItemModel(
            name="soup",
            price=23.45,
        ),
        MenuItemModel(
            name="tea",
            price=13.0,
        ),
        MenuItemModel(
            name="pancakes",
            price=7.85,
        ),
    ]
    return menu_data


@pytest_asyncio.fixture
async def order_test_data():
    """
    Функция-фикстура
    """
    order_data = [
        OrderModel(
            table_number=1,
        ),
        OrderModel(
            table_number=1,
        ),
        OrderModel(
            table_number=1,
        ),
    ]
    return order_data


@pytest_asyncio.fixture
async def order_item_test_data():
    """
    Функция-фикстура
    """
    order_item_data = [
        OrderItemModel(
            order=1,
            menu_item=1,
            quantity=2,
        ),
        OrderItemModel(
            order=1,
            menu_item=2,
            quantity=2,
        ),
        OrderItemModel(
            order=1,
            menu_item=3,
            quantity=5,
        ),
        OrderItemModel(
            order=2,
            menu_item=2,
            quantity=3,
        ),
        OrderItemModel(
            order=2,
            menu_item=3,
            quantity=3,
        ),
        OrderItemModel(
            order=3,
            menu_item=1,
            quantity=5,
        ),
    ]
    return order_item_data
