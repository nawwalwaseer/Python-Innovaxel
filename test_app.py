import pytest
import asyncio
from app import fetchUsers, fetchOrders, fetchProducts, main
from app import find_max_min, reverse_words

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

def test_find_max_min():
    numbers = [10, 20, 3, 40, 5]
    result = find_max_min(numbers)
    assert result == (40, 3)


def test_find_max_min_empty():
    with pytest.raises(ValueError):
        find_max_min([])


def test_reverse_words():
    sentence = "Hello World from Python"
    result = reverse_words(sentence)
    assert result == "Python from World Hello"


def test_reverse_words_type_error():
    with pytest.raises(TypeError):
        reverse_words(12345)