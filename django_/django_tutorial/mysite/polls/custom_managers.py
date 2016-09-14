from django.db import models
from .custom_querysets import PersonQuerySet

# A custom Manager that shows how you can execute raw SQL statement.
class PollManager(models.Manager):
    def with_counts(self):
        from django.db import connection

        with connection.cursor() as cursor:
            cursor.execute("""SELECT p.id, p.question, p.poll_date, COUNT(*)
                FROM polls_opinionpoll p, polls_response r
                WHERE p.id = r.poll_id
                GROUP BY p.id, p.question, p.poll_date
                ORDER BY p.poll_date DESC""")
            result_list = []
            for row in cursor.fetchall():
                # We create an anonymous object here with the row data
                obj = type('', (object,),
                           {'id': row[0], 'question': row[1], 'poll_date': row[2], 'num_responses': row[3]})()
                result_list.append(obj)
        return result_list


# A custom manager which will override the base QuerySet for the Book model. The custom manager will always filter
# on the author field which matches the name 'Roald Dahl' before returning the queryset.
class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super(DahlBookManager, self).get_queryset().filter(authors__name='Roald Dahl')


# A custom manager which uses a custom QuerySet.
class PersonManager(models.Manager):

    def get_queryset(self):
        return PersonQuerySet(self.model, using=self._db)

    def authors(self):
        return self.get_queryset().authors()

    def editors(self):
        return self.get_queryset().editors()
