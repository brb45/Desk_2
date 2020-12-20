import requests
import unittest

def api():
    response = requests.get('https://www.google.com/')
    return response

if api() == 200:
    print(True)


class TetsApiNoMock(unittest.TestCase):

    def test_api(self):
        assert api().status_code == 200


import unittest
from unittest.mock import Mock
from unittest.mock import patch
import requests
import unittest


class TetsApi(unittest.TestCase):

    def test_api_no_mock(self):
        assert api().status_code == 200

    def test_api_mock(self):
        with patch.object(requests, 'get') as get_mock:
            get_mock.return_value = mock_response = Mock()
            mock_response.status_code = 200
            assert api().status_code == 200

if __name__ == '__main__':
    unittest.main(verbosity=2)