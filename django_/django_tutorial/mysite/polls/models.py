from django.db import models
from django.utils import timezone
import datetime

from sqlalchemy.ext import orderinglist


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # These fields are used by the django admin site to provide sort capabilities, glyph icon, and a column header
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# =========================== MANY-TO-MANY ======================================
# The topping and pizza models will have a ManyToMany relationship
class Topping(models.Model):
    ingredient = models.CharField(max_length=200)
    perishable_date = models.DateField()


class Pizza(models.Model):
    name = models.CharField(max_length=100)
    toppings = models.ManyToManyField(Topping)


# =========================== MANY-TO-MANY WITH INTERMEDIATE ENTITY ======================================
# This is an example of defining an intermediate entity between Person and Group through the Membership entity.
class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Group(models.Model):
    group_name = models.CharField(max_length=100)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.group_name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=255)


# =========================== ONE-TO-ONE ======================================
# This example shows how you model a One-To-One relationship with entities Place and Restaurant.
# It basically models an inheritance, where an Restaurant "is a" Place.
class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    # You can override the save() method on a concrete Model implementation.
    def save(self, *args, **kwargs):
        print('Override the save method() before')
        super(Place, self).save(*args, **kwargs)  # Call the real save() method on the parent
        print('Override the save method() after')


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, primary_key=True)
    serves_burgers = models.BooleanField(default=False)
    serves_sushi = models.BooleanField(default=False)

    def __str__(self):
        return "%s Restaurant" % self.place.name


# =========================== MODEL META Options ======================================
# This example shows how you can add a Meta class to your Model class to provide more functionality.
# The models below show how you can create an abstract model, and how it's implementation can override it's parent Meta class

class CommonInfo(models.Model):
    label = models.CharField(max_length=255)
    visible = models.BooleanField(default=False)

    class Meta:
        abstract = True  # This will make the CommonInfo entity abstract, and will not create a table for it.
        ordering = ["label"]


class Product(CommonInfo):
    description = models.CharField(max_length=255)

    class Meta(CommonInfo.Meta):
        db_table = 'product_info'


# =========================== PROXY MODEL ======================================
# This example shows how you can create a Proxy model, which is similar to a concrete implementation, but doesn't create
# a physical table, sort of like an adapter for your model.

class ProxyPerson(Person):
    class Meta:
        proxy = True
        ordering = ['last_name']

    def __str__(self):
        return "The Proxy Person entity with %s %s" % (self.first_name, self.last_name)


# =========================== BLOGGING MODEL ======================================
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, related_name='entries')
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline
