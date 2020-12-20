from unittest.mock import patch

from unittest import TestCase

from apps_1 import call_external_api

import unittest


class MockResponse:

    def __init__(self):
        self.status_code = 200

    def json(self):
        return {
            "week_number": 18,
            "utc_offset": "+02:00",
            "utc_datetime": "2020-04-30T10:48:54.398875+00:00",
            "unixtime": 1588243734,
            "timezone": "Europe/Rome",
            "raw_offset": 3600,
            "dst_until": "2020-10-25T01:00:00+00:00",
            "dst_offset": 3600,
            "dst_from": "2020-03-29T01:00:00+00:00",
            "dst": True,
            "day_of_year": 121,
            "day_of_week": 4,
            "datetime": "2020-04-30T12:48:54.398875+02:00",
            "client_ip": "91.252.18.0",
            "abbreviation": "CEST"
        }


class TestExternalAPI(TestCase):

    @patch("requests.get", return_value=MockResponse())
    def test_call_external_api(self, mocked):
        self.assertEqual(
            call_external_api(),
            "2020-04-30T12:48:54.398875+02:00"
        )