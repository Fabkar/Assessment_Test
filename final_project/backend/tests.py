from django.test import TestCase
from backend.models import Client

# Create your tests here.
class Test_user(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.dummy = Client.objects.create(gov_id="F0008G",
                                        first_name="Fabian",
                                        last_name="Carmona",
                                        email="test@gmail.com",
                                        company="retailer company",
                                        )

    def test_allusers(self):
        users = Client.objects.all()
        self.assertEquals(users.count(), 1)

    def test_quiery_specific(self):
        query = Client.objects.filter(first_name="Fabian")
        print(query)
        self.assertEqual(query.first_name,"Fabian")
