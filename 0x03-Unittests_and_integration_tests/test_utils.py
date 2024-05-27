#!/usr/bin/env python3
"""
Unit tests for access_nested_map function in utils.py
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test that access_nested_map returns the expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that access_nested_map raises a KeyError as expected"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(
            str(cm.exception),
            f"'{path[-1]}'"
        )


class TestGetJson(unittest.TestCase):
    """Test cases for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the expected result"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        with patch('utils.requests.get', return_value=mock_response) as (
                mock_get : result=get_json(test_url)
                self.assertEqual(result, test_payload)
                mock_get.assert_called_once_with(test_url))


if __name__ == '__main__':
    unittest.main()
