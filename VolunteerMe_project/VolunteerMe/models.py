from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)
    # The additional attributes we wish to include.
    TYPE_CHOICES = (('v','Volunteer'),('o','organiser'))
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=128,help_text='Full Name')
    email = models.EmailField(help_text='Email')
    contact_number = models.CharField(max_length=15, help_text='Contact number')
    post_code = models.CharField(max_length=12,blank=True,help_text='postcode')
    address = models.CharField(max_length=128,blank=True,help_text='address')
    town = models.CharField(max_length=128,blank=True,help_text='Town')
    picture = models.ImageField(upload_to='profile_images', blank=True)

# Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

# class Category(models.Model):
#     CAT_CHOICES = (
#         ('A', 'Administrative / Office Work'), ('B', 'Advice / Information giving'), ('C', 'Advocacy / Human Rights)'),
#         ('D', 'Arts ( music/drama/crafts)'), ('E', 'Befriending / Mentoring'), ('F', 'Campaigning / Lobbying'),
#         ('G', 'Care / Support worker'), ('H', 'Catering'), ('I', 'Charity Event Support'),
#         ('J', 'Charity Shops / Retail'),
#         ('K', 'Committee Work'),
#         ('L', 'Community / Economic Development Work'), ( 'M', 'Computing'), ('N', 'Conservation / Gardening'),
#         ('O', 'Counselling'),
#         ('P', 'Disaster / emergency relief'), ('Q', 'Drivers'), ('R', 'Driving / escorting'),
#         ('S', 'Equal Opportunities / Race relations'), ('T', 'Event Management'), ( 'U', 'Event Marshals'),
#         ('V', 'Finance / Accountancy'), ( 'W', 'Fundraising'), ('X', 'General Event Support'),
#         ('Y', 'Homebased Volunteering'), ( 'Z', 'IT Support'), ('t', 'Justice / Legal assistance'),
#         ('a', 'Landscaping/course layout/maintenance'), ('b', 'Languages / translating'),
#         ('c', 'Library / Information Management'), ('d', 'Management / Business Skills'),
#         ('e', 'Marketing / PR / Media'), ('f', 'Medical/Physiotherapy'), ('g', 'On line Volunteering'),
#         ('h', 'Playschemes / Childrens Clubs'),
#         ('i', 'Practical /DIY'), ('j', 'Research / Policy work'), ('k', 'Residential volunteering'),
#         ('l', 'Security'),
#         ('m', 'Short term / seasonal working'), ( 'n', 'Specialist / Technical'), ('o', 'Sports / Outdoor activities'),
#         ('p', 'Technical Support'), ('q', 'Tutoring / Supporting Learners'), ( 'r', 'Volunteering for under 16s'),
#         ('s', 'Youth Work'))
#
#     category = models.CharField(max_length=1, choices=CAT_CHOICES)
#     slug = models.SlugField(unique=True)
#
#     def save(self, *args, **kwargs):
#         self.slug = slugify(self.category)
#         super(Category, self).save(*args, **kwargs)
#
#     def __unicode__(self):
#         return self.category


class Opportunity(models.Model):
    name = models.CharField(max_length=128)
    category = models.CharField(max_length=128,default = "Other")
    company = models.ForeignKey(UserProfile, default=None)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    description = models.TextField(blank=True)
    location = models.TextField(blank=True, default="")
    optional = models.TextField(blank=True, default="None")

    def __unicode__(self):
        return self.name


class Application(models.Model):
    volunteer = models.ForeignKey(User)
    opportunity = models.ForeignKey(Opportunity)


class Reply(models.Model):
    application = models.ForeignKey(Application)

    class Meta:
        verbose_name_plural = 'Replies'
