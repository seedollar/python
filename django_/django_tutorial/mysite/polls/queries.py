from django.db.models import F
from django.db.models import Q
from django.db import models, connection
from .models import Entry, Person


# Use this custom class to document how to make queries.
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

    # An example of how to use a limit
    def find_all_entries_with_limit(self, limit):
        return Entry.objects.all()[:limit]

    # An example of how to use an offset and limit
    def find_all_entries_with_offset_and_limit(self, offset, limit):
        return Entry.objects.all()[offset:limit]

    # An example of how to use a index to return only one result from a list
    def find_single_entry_for_rating(self, rating):
        return Entry.objects.filter(rating=rating)[0]

    # An example of how to lookup using the field lookup 'iexact' which is case-insensitive
    def find_entry_iexact_headline(self, headline):
        return Entry.objects.filter(headline__iexact=headline)

    # An example of how to lookup using the field lookup 'contains' which is case-sensitive.
    # You can use the 'icontains' for case-insensitive lookups.
    def find_entry_contains_headline(self, headline):
        return Entry.objects.filter(headline__contains=headline)

    # An example of using the field lookup 'startswith' which is case-sensitive
    # You can use the 'istartswith' for case-insensitive lookups.
    def find_entry_startswith_headline(self, headline):
        return Entry.objects.filter(headline__startswith=headline)

    # An example of using the field lookup 'endswith' which is case-sensitive
    # You can use the 'iendswith' for case-insensitive lookups.
    def find_entry_endswith_headline(self, headline):
        return Entry.objects.filter(headline__endswith=headline)

    # An example of how you can span relationships among entities in your queries.
    # In this case we are using the entry's blog 'name' attribute in our predicate.
    def find_entry_for_blog_name(self, blog_name):
        return Entry.objects.filter(blog__name=blog_name)

    # An example of 'isnull' field lookup
    def find_entries_for_null_authors(self):
        return Entry.objects.filter(authors__isnull=True)

    # An example of 'in' field lookup
    def find_entries_with_pks_in(self, ids):
        return Entry.objects.filter(pk__in=ids)

    # An example of how to the filter expression can reference fields on the model using the 'F()' function.
    def find_entries_ncomments_gte_npingbacks(self):
        return Entry.objects.filter(n_comments__gte=F('n_pingbacks'))

    # An example of how you can apply arithmetic operations on an 'F()' function expression
    # Here we get all entries who rating value is less-than-or-equals to the sum of n_comments and n_pingbacks.
    def find_entries_with_ratings_lte_hits(self):
        return Entry.objects.filter(rating__lte=F('n_comments') + F('n_pingbacks'))

    # An example of how to use the 'Q()' function
    def find_entries_with_headline_startswith_q1_or_q2(self, q1, q2):
        return Entry.objects.filter(Q(headline__startswith=q1) | Q(headline__startswith=q2))

    # An example of how you can clone models. Note that relations are not cloned.
    def copy_entry_for_pk(self, id):
        entry_result = Entry.objects.get(pk=id)
        new_entry = entry_result
        # we can simply set the id to None so that it creates a new record
        new_entry.id = None
        new_entry.save()
        return new_entry;

    # An example of how to update multiple entries using the update() method.
    def update_entries_for_rating(self, rating, headline):
        Entry.objects.filter(rating=rating).update(headline=headline)

    # An example of the 'select_related()' function which will eagerly load the entry and it's relations
    # by caching them.z
    def fully_load_entry_for_pk(self, id):
        return Entry.objects.select_related(pk=id)


# This custom manager will illustrate how we can execute RAW SQL statements in Django
class RawSQLManager(models.Manager):

    # This snippet shows how you can invoke the raw() method with a plain SQL statement.
    # It will return a RawQuerySet object.
    def get_all_persons(self):
        return Person.peeps.raw("SELECT * FROM polls_person")

    # This example shows how you can map another table's names to the Person model using the
    # translations attribute and a dictionary of field mappings.
    def get_persons_using_translation(self):
        field_map = {'first': 'first_name', 'last': 'last_name'}
        return Person.peeps.raw("SELECT * from polls_anotherperson", translations=field_map)

    # You can also use indexing/slicing with a raw() function
    def get_first_person(self):
        return Person.peeps.raw("SELECT * FROM polls_person LIMIT 1")[0]

    # This example shows how you can pass parameters to the raw() function
    def get_person_for_role(self, role):
        return Person.peeps.raw("SELECT * FROM polls_person where role = %s", [role])

    # An example of how we can execute a SQL statement directly using the connection and cursor objects
    def get_books_for_rating_greater_than(self, rating):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM polls_book WHERE rating > %s", [rating])
            return cursor.fetchall()
