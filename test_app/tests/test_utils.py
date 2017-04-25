import json
from unittest import TestCase

import requests_mock

from django_http_model.utils import RequestUtils


class RequestUtilsTest(TestCase):

    def test_should_fetch_correct_json_when_json_is_passed(self):
        company_dict = {
            "name": "Company 1",
            "id": 1,
            "nameOfFounder": "Marcos Cardoso",
            "birthday": "2017-04-19",
        }

        url = "http://my.api.com/companies/1"

        with requests_mock.mock() as m:
            m.get(url, text=json.dumps(company_dict))
            response = RequestUtils.fetch_from_url(url)
            self.assertDictEqual(company_dict, response)