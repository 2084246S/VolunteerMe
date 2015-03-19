from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Vol(models.Model):
    TYPE_CHOICES = (('v','Volunteer'),('o','organiser'))
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)

class Volunteer(models.Model):
    user = models.OneToOneField(User,unique=True)
    firstname = models.CharField(max_length=128)
    surname = models.CharField(max_length=128)
    email = models.EmailField()
    gender = models.CharField(max_length=32, choices=((1, "Male"), (2, "Female"), (3, "Other")))
    time_available = models.DateField()
    contact_number = models.CharField(max_length=15, blank=True)
    post_code = models.CharField(max_length=12,blank=True)
    address = models.CharField(max_length=128,blank=True)
    town = models.TextField(blank=True)


    def __unicode__(self):
        return self.user.username


class Category(models.Model):

    job_name = models.CharField(max_length=128, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Search(models.Model):
    town_or_postcode = models.CharField(max_length=128, blank=True)
    distance_from = models.IntegerField(blank=True)
    category = models.ForeignKey(Category)
    optional = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Organiser(models.Model):
    user = models.OneToOneField(User,unique=True)
    company_name = models.CharField(max_length=128, unique=True)
    company_email = models.EmailField()
    company_number = models.IntegerField()
    company_address = models.CharField(max_length=128)
    company_post_code = models.CharField(max_length=12,blank=True)
    company_town = models.TextField(blank=True)

    def __unicode__(self):
        return self.user.username


class Opportunity(models.Model):
    name = models.CharField(max_length=128, unique=True)
    category = models.CharField(max_length=128, default="Other")
    company = models.ForeignKey(Organiser, default=None)
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
