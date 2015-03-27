from datetime import date

from django.test import TestCase, RequestFactory
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from VolunteerMe.models import UserProfile, Opportunity, Reply, Application
#helper methods
def adduser(username,email,password):
    user = User.objects.create_user(username,email,password)
    user.save()
    return user

def addprofile(user,name,type,email,contact_number):
    userprofile = UserProfile.objects.create(user=user,name=name,type=type,email=email,contact_number=contact_number)
    userprofile.save()
    return userprofile

def addopportunity(name,category,company,start_date,end_date,description,location,optional):
    opp = Opportunity.objects.create(name=name,category=category,company=company,start_date=start_date,
                                     end_date=end_date,description=description,location=location,optional=optional)
    opp.save()
    return opp


class IndexViewTests(TestCase):
    def test_index_view_with_no_categories(self):
        """
        If no questions exist, an appropriate message should be displayed.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['new_opportunities'], [])

    def tset_index_with_opps(self):
        user = adduser("testUser", "testemail@example.com", "testpassword")
        userprofile = addprofile(user=user, name="Test", type='o', email="testemail@example.com",
                                 contact_number='0123456789')
        addopportunity(name="Admin", category="Administrative / Office Work",
                       company=userprofile,
                       start_date=date.today(), end_date=date.today(),
                       description="Helping with the finances for a community center",
                       location="4 Privet Drive, Surrey",
                       optional="must be good with children")

        addopportunity( name="Cleaning", company=userprofile, description="Janitorial duties ",
                        location="Just down the road", category = 'Community / Economic Development Work' ,start_date=date.today(), end_date=date(2015,04,23))
        addopportunity( name="Something Completely Different", company=userprofile,
                        description="You are expected to clean the surface of mars with a toothbrush.", location="Mars",
                        category = 'Other' ,start_date=date.today(), end_date=date(2016,03,07))
        addopportunity( name="Running Around Shouting at People",  company=userprofile,description="Command position on new space mission", location="The moon",
                        category = 'Management / Business Skills' ,start_date=date.today(), end_date=date(2016,05,07))
        addopportunity( name="Performing Open Heart Surgery", company=userprofile,
                        description="Please do not kill your patients.", location="84 Castle Street, Glasgow",
                        category = 'Medical/Physiotherapy' ,start_date=date.today(), end_date=date(2015,12,07))
        addopportunity( name="Child mentoring", company=userprofile, description="Helping children", location="4 Privet Drive,Surrey",
                        category = 'Befriending / Mentoring' ,start_date=date.today(), end_date=date(2015,05,07))
        addopportunity(name="Shining Spoons", company=userprofile, description="Cleaning cutlery for the holidays",
                       location="The land of cutlery",category = 'Short term / seasonal working', start_date=date.today(), end_date=date(2015,06,04))

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['new_opportunities'], Opportunity.objects.order_by('-start_date')[:5])
        self.assertQuerysetEqual(response.context['ending_soon'],Opportunity.objects.order_by('end_date')[:5])


class OpportunityViewTests(TestCase):
    def testopppage(self):

        user = adduser("testUser", "testemail@example.com", "testpassword")
        userprofile = addprofile(user=user, name="Test", type='o', email="testemail@example.com",
                                 contact_number='0123456789')
        opportunity =addopportunity(name="Admin", category="Administrative / Office Work",
                            company=userprofile,
                            start_date=date.today(), end_date=date.today(),
                            description="Helping with the finances for a community center",
                            location="4 Privet Drive, Surrey",
                            optional="must be good with children")


        response = self.client.get(reverse('opportunity/(?P<opportunity_id>\d+',{{opportunity}}))
        self.assertEqual(response.status_code, 200)
        # self.assertContains(response, "There are no categories present.")
        self.assertQuerysetEqual(response.context['company'] , opportunity.company)
        self.assertQuerysetEqual(response.context['opportunity_name'] , opportunity.name)
        self.assertQuerysetEqual(response.context['start_date'] , opportunity.start_date)
        self.assertQuerysetEqual(response.context['end_date'] , opportunity.end_date)
        self.assertQuerysetEqual(response.context['description'] , opportunity.description)
        self.assertQuerysetEqual(response.context['optional'] , opportunity.optional)
        self.assertQuerysetEqual(response.context['location'] , opportunity.location)




# Create your tests here.

class SearchViewTests(TestCase):
    def test_search_with_no_parameters(self):
        response = self.client.get(reverse('search'))
        self.assertQuerysetEqual(response.context['result_list'], Opportunity.objects.all())


class ProfileTestCase(TestCase):
    def setUp(self):
        user = adduser("testUser", "testemail@example.com", "testpassword")
        addprofile(user=user, name="Test", type='o', email="testemail@example.com",
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
        user = adduser("testUser", "testemail@example.com", "testpassword")
        userprofile = addprofile(user=user, name="Test", type='o', email="testemail@example.com",
                                 contact_number='0123456789')
        opportunity = addopportunity(name="Admin", category="Administrative / Office Work",
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
        user = adduser("testUser1", "testemail1@example.com", "testpassword1")


        userprofile = addprofile(user=user, name="Test1", type='o', email="testemail1@example.com",
                                 contact_number='0123456789')

        user2 = adduser("testUser2", "testemail2@example.com", "testpassword2")


        userprofile2 = addprofile(user=user2, name="Test2", type='v', email="testemail2@example.com",
                                  contact_number='987654321')

        opportunity = addopportunity(name="Admin", category="Administrative / Office Work",
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