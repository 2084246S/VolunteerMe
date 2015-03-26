from datetime import date

from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from VolunteerMe.models import UserProfile, Opportunity, Reply, Application


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['new_opportunities'], [])


# Create your tests here.

class SearchViewTests(TestCase):
    def test_search_with_no_parameters(self):
        response = self.client.get(reverse('search'))
        self.assertQuerysetEqual(response.context['result_list'], Opportunity.objects.all())


class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("testUser", "testemail@example.com", "testpassword")
        user.save()

        userprofile = UserProfile.objects.create(user=user, name="Test", type='o', email="testemail@example.com",
                                                 contact_number='0123456789')

    def test_profile(self):
        user = User.objects.get(username="testUser")
        userprofile = UserProfile.objects.get(user=user)
        # assert user attributes
        self.assertEqual(user.username, "testUser")
        self.assertEqual(user.email, "testemail@example.com")
        self.assertEqual(userprofile.name, "Test")
        self.assertEqual(userprofile.email, "testemail@example.com")
        self.assertEqual(userprofile.type, "o")
        self.assertEqual(userprofile.contact_number, "0123456789")
        # testpassword is encoded


class OpportunityTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("testUser", "testemail@example.com", "testpassword")
        user.save()

        userprofile = UserProfile.objects.create(user=user, name="Test", type='o', email="testemail@example.com",
                                                 contact_number='0123456789')

        opportunity = Opportunity.objects.create(name="Admin", category="Administrative / Office Work",
                                                 company=userprofile,
                                                 start_date=date.today(), end_date=date.today(),
                                                 description="Helping with the finances for a community center",
                                                 location="4 Privet Drive, Surrey",
                                                 optional="must be good with children")

    def testOpp(self):
        user = User.objects.get(username="testUser")
        userprofile = UserProfile.objects.get(user=user)
        opportunity = Opportunity.objects.get(company=userprofile)
        # assert user attributes
        self.assertEqual(opportunity.name, "Admin")
        self.assertEqual(opportunity.category, "Administrative / Office Work")
        self.assertEqual(opportunity.start_date, date.today())
        self.assertEqual(opportunity.end_date, date.today())
        self.assertEqual(opportunity.description, "Helping with the finances for a community center")
        self.assertEqual(opportunity.location, "4 Privet Drive, Surrey")
        self.assertEqual(opportunity.optional, "must be good with children")
        # testpassword is encoded


class ApplicationTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user("testUser1", "testemail1@example.com", "testpassword1")
        user.save()

        userprofile = UserProfile.objects.create(user=user, name="Test1", type='o', email="testemail1@example.com",
                                                 contact_number='0123456789')

        user2 = User.objects.create_user("testUser2", "testemail2@example.com", "testpassword2")
        user2.save()

        userprofile2 = UserProfile.objects.create(user=user2, name="Test2", type='v', email="testemail2@example.com",
                                                  contact_number='987654321')

        opportunity = Opportunity.objects.create(name="Admin", category="Administrative / Office Work",
                                                 company=userprofile,
                                                 start_date=date.today(), end_date=date.today(),
                                                 description="Helping with the finances for a community center",
                                                 location="4 Privet Drive, Surrey",
                                                 optional="must be good with children")

        application = Application.objects.create(volunteer=user2, opportunity=opportunity)

    def testapp(self):
        user = User.objects.get(username="testUser1")
        userprofile = UserProfile.objects.get(user=user)
        user2 = User.objects.get(username="testUser2")
        userprofile2 = UserProfile.objects.get(user=user2)
        opportunity = Opportunity.objects.get(company=userprofile)

        application = Application.objects.get(opportunity=opportunity)

        self.assertEquals(application.volunteer, user2)