import time
from unittest import TestCase

from test_app.models import Company


class HTTPModelManagerTest(TestCase):

    def test_should_instantiate_company(self):
        company_dict = {
            "name": "Company 1",
            "id": 1,
            "nameOfFounder": "Marcos Cardoso",
            "birthday": "2017-04-19",
        }

        manager = Company.objects()
        instance = manager._HTTPModelManager__create_instance(company_dict)

        self.assertIsInstance(instance, Company)
        self.assertEqual(instance.name, "Company 1")
        self.assertEqual(instance.company_id, 1)
        self.assertEqual(instance.founder, "Marcos Cardoso")
        self.assertEqual(instance.birthday, time.strptime("2017-04-19", "%Y-%m-%d"))
