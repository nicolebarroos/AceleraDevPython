from main import get_temperature
import requests
import pytest


#Ref: https://docs.pytest.org/en/5.4.2/monkeypatch.html

class MockResponse:
    @staticmethod
    def json():
        return { "currently": { "temperature": 62 } }

    def test_get_json(monkeypatch):
        def mockget(*args, **kwargs):
            return MockResponse()

        monkeypatch.__setattr__(requests, "get", mock_get)


@pytest.mark.parametrize("lat, lng, expect", [(-14.235004, -51.92528, 16)])
def test_get_temperature_by_lat_lng(lat, lng, expect, monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr(requests, "get", mock_get)
    result = get_temperature(lat, lng)

    assert result == expect