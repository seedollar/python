# This python file will contain a Database Manager object which will illustrate how to perform
# database aggregate functions on models.
from django.db import models
from .models import Author, Publisher, Book, Store
from django.db.models import Avg, Max, Sum, F, Count, Min

class AggManager(models.Manager):


    # Example of how to count the number of records on a given model
    def count_books(self):
        return Book.objects.count()

    # Example of how to use the aggregate() method in conjunction with the Avg class
    def calc_average_book_price(self):
        return Book.objects.aggregate(Avg('price'))

    # Example of how to use the aggregate() method in conjunction with the Max class
    def calc_max_book_price(self):
        return Book.objects.aggregate(Max('price'))

    # Example of how to use the aggregate() method in conjunction with the F class
    def calc_cost_per_page(self):
        return Book.objects.aggregate(price_per_page=Sum(F('price')/F('pages'), output_field=models.FloatField()))

    # Example of how to use the aggregate() method with many aggregate Classes as parameters
    def calc_aggregations_on_book_price(self):
        return Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))

    # Example of how to use the annotate() method to create a real-time field named 'num_books' on each publisher model.
    # Note the output of the annotate() method is a QuerySet object, which means you can apply further filter()
    # and order_by() functions on the result.
    def annotate_publisher_with_realtime_field(self):
        return Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')


