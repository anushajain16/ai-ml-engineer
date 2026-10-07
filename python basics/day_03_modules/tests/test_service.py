import pytest
import day_03_modules.exercises.service as service
import unittest.mock as mock
import requests

@mock.patch("day_03_modules.exercises.service.get_user_by_id")
def test_get_user_by_id(mock_get):
    mock_get.return_value = "Anusha"
    result = service.get_user_by_id("1")
    assert result == "Anusha"

@mock.patch("day_03_modules.exercises.service.get_user")
def test_get_user(mock_get):
    mock_get.return_value = [{"id": 1, "name": "Anusha"}]
    result = service.get_user()
    assert result == [{"id": 1, "name": "Anusha"}]
