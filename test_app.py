import pytest
import asyncio
from app import fetchUsers, fetchOrders, fetchProducts, main

@pytest.mark.asyncio
async def test_fetchUsers():
    result = await fetchUsers()
    assert result == "Users Fetched!"

@pytest.mark.asyncio
async def test_fetchOrders():
    result = await fetchOrders()
    assert result == "Orders Fetched!"

@pytest.mark.asyncio
async def test_fetchProducts():
    result = await fetchProducts()
    assert result == "Products Fetched!"

@pytest.mark.asyncio
async def test_main():
    results = await main()
    assert results == ["Users Fetched!", "Orders Fetched!", "Products Fetched!"]
