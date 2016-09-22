from django.db import models
from .models import Properties

# A custom manager for the Properties model to illustrate how we use the 'using()' method to specify
# which database to access for the query.
class PropertiesManager(models.Manager):

    # An illustration of the 'using()' method to retrieve the Properties from the provided database_alias parameter
    def get_all_properties_using(self, database_alias):
        return Properties.objects.using(database_alias).all()

    # This method takes 3 arguments, the database alias, and key/value pair to save.
    def create_properties_using(self, key, value, database_alias):
        Properties.objects.using(database_alias).create(key=key, value=value)

    # This method illustrates how you can use the 'using()' method on the save() method
    def save_key_value_using(self, key, value, database_alias):
        property = Properties(key=key, value=value)
        property.save(using=database_alias)




