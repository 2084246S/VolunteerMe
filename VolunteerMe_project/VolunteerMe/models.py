from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class UserProfile(models.Model):


    user = models.OneToOneField(User)
    is_volunteer = models.BooleanField()


    def __unicode__(self):
        return self.user.username





class Intern(UserProfile):

    gender = models.ChoiceField(initial=None, help_text='Gender')
    time_available =models.ChoiceField(initial=None, help_text='times available')


    def __unicode__(self):


        return self.user.username


    class Meta:


        ordering = ['user__last_name', 'user__first_name', ]


class Recruiter(UserProfile):


        company_name = models.CharField(max_length=20, unique=True)
    company_description = models.CharField(max_length=400)
    url = models.URLField(max_length=100)


    def __unicode__(self):


        return self.user.username
    ordering = ['company_name']


class Category(models.Model):
    CAT_CHOICES = (
        ('A', 'Administrative / Office Work'), ('B', 'Advice / Information giving'), ('C', 'Advocacy / Human Rights)'),
        ('D', 'Arts ( music/drama/crafts)'), ('E', 'Befriending / Mentoring'), ('F', 'Campaigning / Lobbying'),
        ('G', 'Care / Support worker'), ('H', 'Catering'), ('I', 'Charity Event Support'),
        ('J', 'Charity Shops / Retail'),
        ('K', 'Committee Work'),
        ('L', 'Community / Economic Development Work'), ( 'M', 'Computing'), ('N', 'Conservation / Gardening'),
        ('O', 'Counselling'),
        ('P', 'Disaster / emergency relief'), ('Q', 'Drivers'), ('R', 'Driving / escorting'),
        ('S', 'Equal Opportunities / Race relations'), ('T', 'Event Management'), ( 'U', 'Event Marshals'),
        ('V', 'Finance / Accountancy'), ( 'W', 'Fundraising'), ('X', 'General Event Support'),
        ('Y', 'Homebased Volunteering'), ( 'Z', 'IT Support'), ('t', 'Justice / Legal assistance'),
        ('a', 'Landscaping/course layout/maintenance'), ('b', 'Languages / translating'),
        ('c', 'Library / Information Management'), ('d', 'Management / Business Skills'),
        ('e', 'Marketing / PR / Media'), ('f', 'Medical/Physiotherapy'), ('g', 'On line Volunteering'),
        ('h', 'Playschemes / Childrens Clubs'),
        ('i', 'Practical /DIY'), ('j', 'Research / Policy work'), ('k', 'Residential volunteering'),
        ('l', 'Security'),
        ('m', 'Short term / seasonal working'), ( 'n', 'Specialist / Technical'), ('o', 'Sports / Outdoor activities'),
        ('p', 'Technical Support'), ('q', 'Tutoring / Supporting Learners'), ( 'r', 'Volunteering for under 16s'),
        ('s', 'Youth Work'))

    category = models.CharField(max_length=128, choices=CAT_CHOICES)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.category)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.category


class Search(models.Model):
    town_or_postcode = models.CharField(max_length=128, blank=True)
    distance_from = models.IntegerField(blank=True)
    category = models.ForeignKey(Category)
    optional = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Opportunity(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128, default="Other")
    company = models.ForeignKey(UserProfile, default=None)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    location = models.TextField(blank=True, default="")
    optional = models.TextField(blank=True, default="None")

    def __unicode__(self):
        return self.name


class Application(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    opportunity = models.ForeignKey(Opportunity)


class Reply(models.Model):
    application = models.ForeignKey(Application)

    class Meta:
        verbose_name_plural = 'Replies'
