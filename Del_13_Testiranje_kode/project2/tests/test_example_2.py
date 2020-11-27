import requests
from helpers.example_2 import example2

"""
This file (test_example2.py) contains the unit tests for the example2.py file.
"""


def test_get_response_success(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to successful
    THEN check the HTTP response
    """

    class MockResponse:
        def __init__(self):
            self.status_code = 200
            self.url = "http://www.testurl.com"

        def json(self):
            return {"account": "5678", "url": "http://www.testurl.com"}

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    assert example2() == (200, "http://www.testurl.com")


def test_get_response_failure(monkeypatch):
    """
    GIVEN a monkeypatched version of requests.get()
    WHEN the HTTP response is set to failed
    THEN check the HTTP response
    """

    class MockResponse:
        def __init__(self):
            self.status_code = 404
            self.url = "http://www.testurl.com"

        def json(self):
            return {"error": "bad"}

    def mock_get(url):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    assert example2() == (404, "")
