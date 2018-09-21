"""Tests for complaint_counter.py"""
from urllib.parse import urlencode

from complaint_counter import lambda_handler


def request_body(**kwargs):
    """Create a QS request body, like one provided from a slack request."""
    kwargs.setdefault("token", "ftMJyTJlA4qo8QNY3PVhuYf6")
    kwargs.setdefault("team_id", "T18UTUL93")
    kwargs.setdefault("team_domain", "disjointedimages")
    kwargs.setdefault("channel_id", "D81P2TLNM")
    kwargs.setdefault("channel_name", "directmessage")
    kwargs.setdefault("user_id", "U81JYT64Q")
    kwargs.setdefault("user_name", "maxwellgbrown")
    kwargs.setdefault("command", "/curtis_complained")
    kwargs.setdefault("text", "")
    kwargs.setdefault(
        "response_url",
        "https://hooks.slack.com/commands/T18UTUL93/440741347573"
        "/RSYHp7T18s0uP4eU7hGFdSm6",
    )

    return urlencode(kwargs)


def test_lambda_handler_returns_200():
    """Test that lambda_handler returns a 200 status code."""
    response = lambda_handler({'body': request_body()})
    assert response['statusCode'] == 200


def test_lambda_handler_quotes_the_complaint():
    """Test that the lambda_handler returns the complaint as a quote."""
    complaint = "about foo and bar"
    response = lambda_handler({"body": request_body(text=complaint)})

    assert f'\n> {complaint}' in response['body']
