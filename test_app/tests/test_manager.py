import json
import time
from unittest import TestCase

import requests_mock

from test_app.models import Company


class HTTPModelManagerTest(TestCase):

    def test_should_instantiate_company(self):
        company_dict = {
            "name": "Company 1",
            "id": 1,
            "nameOfFounder": "Marcos Cardoso",
            "birthday": "2017-04-19",
        }

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

    def test_should_return_company_with_id_1(self):
        company_dict = {
            "name": "Company 1",
            "id": 1,
            "nameOfFounder": "Marcos Cardoso",
            "birthday": "2017-04-19",
        }

        with requests_mock.mock() as m:
            m.get("http://my.api.com/companies/1", text=json.dumps(company_dict))

            company = Company.objects.get(pk=1)

            expected_result = Company(
                name="Company 1",
                company_id=1,
                founder="Marcos Cardoso",
                birthday=time.strptime("2017-04-19", "%Y-%m-%d")
            )

            self.assertIsInstance(company, Company)
            self.assertEqual(company.company_id, expected_result.company_id)
            self.assertEqual(company.founder, expected_result.founder)

    def test_should_delete_company_with_id_1(self):
        with requests_mock.mock() as m:
            m.delete("http://my.api.com/companies/1", text=json.dumps({"success": True}))
            deleted = Company.objects.delete(pk=1)
            self.assertTrue(deleted)
