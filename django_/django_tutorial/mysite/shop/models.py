from django.db import models
from django.utils import timezone


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    rewardLevel = models.CharField(max_length=1,
                                   choices=(('B', 'Blue'), ('S', 'Silver'), ('G', 'Gold'), ('P', 'Platinum')),
                                   default='B')
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.rewardLevel)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.name, self.description)


class Order(models.Model):
    order_date = models.DateTimeField()
    total = models.DecimalField(max_digits=7, decimal_places=2)
    items = models.ManyToManyField(Item, through='OrderItem')
    customer = models.ForeignKey(Customer)

    def __str__(self):
        return "%s - TOTAL = %f" % (self.order_date, self.total)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    discount = models.FloatField()


# =================================================================================================
# CROSS CUTTING TABLE - Properties

# We created this model to illustrate how the database router is utilized.
# This table will be created on both apps, namely polls and shop
# We setup the database router to migrate this model to both databases, namely 'default' and 'shop-db'
# We also setup the database router to read queries from the 'shop-db' database
# We also setup the database router to write Properties entries to the 'default' database
# =================================================================================================
class Properties(models.Model):
    key = models.CharField(max_length=100)
    value = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return "[%s - %s]" % (self.key, self.value)

