# The Manager class in this python file will give examples of how to apply search functions on models.
from django.db import models
from .models import Author

class SearchManager(models.Manager):

    # An example of how you can use Postgres's unaccent function. You need to import
    # django.contrib.postgres into your INSTALLED_APPS. This method call will only work
    # on a Postgres database. The unaccent() method will ensure that any character variations
    # in the text will be ignored. For example: 'Hélène' will be matched against 'Helene'
    def find_authors_for_name(self, text):
        return Author.objects.filter(name__unaccent_icontains=text)

    

