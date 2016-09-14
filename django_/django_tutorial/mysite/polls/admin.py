from django.contrib import admin
from .models import Question, Choice, Blog, Entry, Author, Store, Book, Publisher, OpinionPoll, Response, Person

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    # fields = ['pub_date', 'question_text'] # Change the order of fields to be displayed

    # Define different categorizations for your fields
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information:', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]

    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently') # This property displays more columns when viewing the Quesiton in the admin site.

    # Provides a filter option on the pub_date field.
    list_filter = ['pub_date']

    # Provide search capablilities on the admin site for the question_text field
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Blog)
admin.site.register(Entry)

admin.site.register(Author)
admin.site.register(Store)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(OpinionPoll)
admin.site.register(Response)
admin.site.register(Person)

