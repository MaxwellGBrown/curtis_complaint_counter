"""Tests for complaint_counter.py"""
from complaint_counter import lambda_handler


def test_lambda_handler_returns_200():
    """Test that lambda_handler returns a 200 status code."""
    response = lambda_handler({})
    assert response['statusCode'] == 200
