from unittest import mock

import pytest
from unittest.mock import patch, Mock, MagicMock

from mock.example_mock import guess_number, get_ip, magic_number, silly


@patch("mock.example_mock.roll_dice")
def test_guess_number(
        roll_dice: MagicMock
):
    roll_dice.return_value = 3
    assert guess_number(3) == "you won"


@patch("mock.example_mock.requests.get")
def test_get_ip(
        requests_get: MagicMock  # requests_get = requests.get in below function
):
    mock_response = Mock(name="mock response",
                         **{"status_code": 200,
                            "json.return_value": {"origin": "0.0.0.0"}
                            })
    requests_get.return_value = mock_response
    assert get_ip() == "0.0.0.0"
    requests_get.assert_called_with("https://httpbin.org/ip")


@patch("mock.example_mock.random.randint")
def test_magic_number(
        ran: MagicMock
):
    ran.side_effect = [3, 4]
    assert magic_number() == 7


@patch("mock.example_mock.random.randint")
@patch("mock.example_mock.time.time")
@patch("mock.example_mock.requests.get")
def test_silly(
        requests_get: MagicMock,  # requests_get = requests.get in below function
        mock_time: MagicMock,    # order should be reverse
        mock_rand: MagicMock
):
    test_param = {
            'number': '5',
            'timestamp': '1639495427.3558776'
    }

    mock_rand.return_value = test_param['number']
    mock_time.return_value = test_param['timestamp']

    mock_response = Mock(name="mock response",
                         **{"status_code": 200,
                            "json.return_value": {'args': test_param,
                                                  }
                            })
    requests_get.return_value = mock_response
    assert silly() == test_param
    requests_get.assert_called_with("https://httpbin.org/get", test_param)
