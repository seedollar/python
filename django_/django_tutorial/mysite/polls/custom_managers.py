import datetime
from django.db import models
from .models import Entry


class EntryManager(models.Manager):

    def find_all_entries(self):
        return Entry.objects.all()

    # Use the get() method to find by ID
    def find_by_id(self, id):
        return Entry.objects.get(pk=id)

    # An example of how to filter on a QuerySet
    def find_entries_for_rating(self, rating):
        return Entry.objects.filter(rating=rating)

    # An example of how to chain filter expressions
    def find_entries_for_headline_not_now(self, keyword):
        return Entry.objects.filter(headline__contains=keyword).exclude(pub_date=datetime.date.today())