import json
from unittest import TestCase

import requests_mock

from test_app.models import Company


class HTTPModelTest(TestCase):

    def test_should_delete_company_instance(self):

        company_dict = {
            "name": "Company 1",
            "id": 1,
            "nameOfFounder": "Marcos Cardoso",
            "birthday": "2017-04-19",
        }

        with requests_mock.mock() as m:
            m.get("http://my.api.com/companies/1", text=json.dumps(company_dict))
            m.delete("http://my.api.com/companies/1", text=json.dumps({"success": True}))

            company = Company.objects.get(pk=1)
            deleted = company.delete()
            self.assertTrue(deleted)
