from zlicutils.tan import TanManager
import pytest
from fastapi import HTTPException


class RequestMock:
    def __init__(self, headers):
        self.headers = headers


def test_init_tan_manager():
    assert TanManager()


def test_no_header():
    tan_manager = TanManager(815)
    with pytest.raises(HTTPException):
        tan_manager.verify_tan(RequestMock({"Dummy": "xxx"}))


def test_invalid_tan():
    tan_manager = TanManager(815)
    with pytest.raises(HTTPException):
        tan_manager.verify_tan(RequestMock({"Flexidug-Authorization-TAN": "123456"}))


def test_valid_tan_only_once():
    tan_manager = TanManager(815)
    tan_manager.verify_tan(RequestMock({"Flexidug-Authorization-TAN": "113358"}))
    with pytest.raises(HTTPException):
        tan_manager.verify_tan(RequestMock({"Flexidug-Authorization-TAN": "113358"}))


def test_html_view():
    tan_manager = TanManager(815)
    assert tan_manager.tans_as_html().status_code == 200
