import time
from unittest import TestCase
import json

from test_app.models import Company

import requests_mock


class HTTPModelManagerTest(TestCase):

    def test_should_instantiate_company(self):
        company_dict = {
            "name": "Company 1",
            "id": 1,
            "nameOfFounder": "Marcos Cardoso",
            "birthday": "2017-04-19",
        }

        # manager =
        instance = Company.objects._HTTPModelManager__create_instance(company_dict)

        self.assertIsInstance(instance, Company)
        self.assertEqual(instance.name, "Company 1")
        self.assertEqual(instance.company_id, 1)
        self.assertEqual(instance.founder, "Marcos Cardoso")
        self.assertEqual(instance.birthday, time.strptime("2017-04-19", "%Y-%m-%d"))

    def test_should_return_all_companies(self):
        companies_list = [
            {
                "name": "Company 1",
                "id": 1,
                "nameOfFounder": "Marcos Cardoso",
                "birthday": "2017-04-19",
            },
            {
                "name": "Company 2",
                "id": 2,
                "nameOfFounder": "Samuel Medeiros",
                "birthday": "2017-04-24",
            }
        ]

        with requests_mock.mock() as m:
            m.get("http://my.api.com/companies", text=json.dumps(companies_list))

            companies = Company.objects.all()

            expected_result = [
                Company(
                    name="Company 1",
                    company_id=1,
                    founder="Marcos Cardoso",
                    birthday=time.strptime("2017-04-19", "%Y-%m-%d")
                ),
                Company(
                    name="Company 2",
                    company_id=2,
                    founder="Samuel Medeiros",
                    birthday=time.strptime("2017-04-24", "%Y-%m-%d")
                ),
            ]

            self.assertIsInstance(companies, list)
            self.assertEqual(len(companies_list), 2)
            self.assertEqual(companies[0].founder, expected_result[0].founder)
