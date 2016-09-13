from django.db import models

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
                print("Row: ", row[0], row[1], row[2])
                # p = self.(id=row[0], question=row[1], poll_date=row[2])
                # p.num_responses = row[3]
                # result_list.append(p)
        return self
