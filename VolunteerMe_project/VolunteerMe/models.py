from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)


    # The additional attributes we wish to include.
    TYPE_CHOICES = (('v', 'volunteer'), ('o', 'organiser'))
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=128,)
    email = models.EmailField()
    contact_number = models.CharField(max_length=15)
    post_code = models.CharField(max_length=12, blank=True)
    address = models.CharField(max_length=128, blank=True)
    town = models.CharField(max_length=128, blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username


class Volunteer(models.Model):
    gender = models.CharField(max_length=32, choices=((1, "Male"), (2, "Female"), (3, "Other")))
    time_available = models.DateField()

    def __unicode__(self):
        return self.user.username


#class Organiser(models.Model):
#    company_name = models.CharField(max_length=128, blank=True)
#    company_number = models.IntegerField(blank=True)
#    user = models.ForeignKey(User)
#
#    def __unicode__(self):
#        return self.user.username


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
        ('Y', 'Homebased Volunteering'), ( 'Z', 'IT Support'), ('t','Justice / Legal assistance'),
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
    name = models.CharField(max_length=128, unique=True)
    category = models.CharField(max_length=128, default="Other")
    company = models.ForeignKey(UserProfile, default=None)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    location = models.TextField(blank=True, default="")
    optional = models.TextField(blank=True, default="")

    def __unicode__(self):
        return self.name


class Application(models.Model):
    volunteer = models.ForeignKey(Volunteer)
    opportunity = models.ForeignKey(Opportunity)


class Reply(models.Model):
    application = models.ForeignKey(Application)

    class Meta:
        verbose_name_plural = 'Replies'
