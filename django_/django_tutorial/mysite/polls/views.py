from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
import logging
from django.contrib.auth import authenticate, login
from django.db import transaction

from .models import Question, Choice, Pizza, Topping, Book

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('mysite')


def landing(request):
    if request.user.is_authenticated:
        logger.debug('User %s is AUTHENTICATED' % request.user)
        return render(request, 'polls/index.html')
    else:
        logger.debug('User is NOT AUTHENTICATED')
        return render(request, 'polls/login.html')


def signin(request):
    logger.debug("INSIDE login() function....")
    username = request.POST.get('username')
    password = request.POST.get('password')
    logger.debug("Credentials username: %s with password: %s" % (username, password))
    user = authenticate(username=username, password=password)
    logger.debug("User authenticated: ", user)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return render(request, 'polls/index.html')
    else:
        # Return an 'invalid login
        return render(request, 'polls/login.html')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        '''Return the last 5 published questions (not including those set to be published in the future'''
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]


# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     context = {'latest_question_list': latest_question_list,}
#     return render(request, "polls/index.html", context)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


# def detail(request, question_id):
#     question = get_object_or_404(Question, id=question_id)
#     return render(request, "polls/detail.html", {"question": question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, "polls/detail.html",
                      {'question': question, 'error_message': "You didn't select a choice!"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))


# View resolver method which tests the atomic request, using the Pizza and Topping models.
# In this example we expect the atomic request to be successful, so we will create a new
# Pizza and 2 Toppings and save them within the request. The response will contain the pizza
# and it's toppings for display. Thus the assumption that the pizza and toppings are bounded to
# the bounded transaction within the request.

# http://localhost:8000/polls/transactions/atomic_request/rollback?topping1=tomato&topping2=carrots&pizza=Tomrot
def atomic_request_success(request):
    topping1 = request.GET['topping1']
    topping2 = request.GET['topping2']
    pizza_name = request.GET['pizza']

    # First persist a new pizza
    new_pizza = Pizza(name=pizza_name)
    new_pizza.save()

    # Now we create and persist the 2 toppings
    toppingOne = Topping.objects.create(ingredient=topping1, perishable_date=timezone.now())
    toppingTwo = Topping.objects.create(ingredient=topping2, perishable_date=timezone.now())

    # Now so assign this pizza the 2 toppings
    new_pizza.toppings.add(toppingOne, toppingTwo)

    return render(request, "polls/atomic_request_results.html", {"pizza": new_pizza,
                                                                 "outcome_message": 'SUCCESS',
                                                                 "pizza_count": Pizza.objects.count(),
                                                                 "topping_count": Topping.objects.count()}
                  )


# =====================================================================================================================
# =====================================================================================================================
# Test the rollback of transactions when ATOMIC_REQUESTS = True
# =====================================================================================================================
# =====================================================================================================================
# We define a mock Exception for the atomic_request_rollback() method below.
class MockRollbackError(Exception):
    pass


# Same as the atomic_request_success() view function, except we will raise an exception after
# saving the pizza and toppings. This should rollback the pizza and toppings with the ATOMIC_REQUESTS = True
#
# http://localhost:8000/polls/transactions/atomic_request/rollback?topping1=tomato&topping2=carrots&pizza=Tomrot
def atomic_request_rollback(request):
    topping1 = request.GET['topping1']
    topping2 = request.GET['topping2']
    pizza_name = request.GET['pizza']

    # First persist a new pizza
    new_pizza = Pizza(name=pizza_name)
    new_pizza.save()

    # Now we create and persist the 2 toppings
    toppingOne = Topping.objects.create(ingredient=topping1, perishable_date=timezone.now())
    toppingTwo = Topping.objects.create(ingredient=topping2, perishable_date=timezone.now())

    new_pizza.toppings.add(toppingOne, toppingTwo)

    # We explicitly raise and Exception here so we rollback
    raise MockRollbackError


# =====================================================================================================================
# =====================================================================================================================
# @transaction.non_atomic_requests
# =====================================================================================================================
# =====================================================================================================================
# This view method will be excluded from the blanket function ATOMIC_REQUESTS = True
# After you invoke this method you can confirm that the pizza total count is still incremented by 1.
@transaction.non_atomic_requests
def atomic_request_skip(request):
    Pizza.objects.create(name='NonAtomicRequested Pizza')
    raise MockRollbackError


# =====================================================================================================================
# =====================================================================================================================
# @transaction.atomic
# =====================================================================================================================
# =====================================================================================================================
# This method simply adds a new pizza to the database. We will use it in the illustration of
# how to use the @transaction.atomic annotation on a view which will call this method, making
# it a part of the same transaction boundary.
def save_a_pizza():
    Pizza.objects.create(name=str(timezone.now()))


# This method simply adds a new topping to the database. We will use it in the illustration of
# how to use the @transaction.atomic annotation on a view which will call this method, making
# it a part of the same transaction boundary.
def save_a_topping():
    Topping.objects.create(ingredient=str(timezone.now()), perishable_date=timezone.now())


# This method simply adds a new book to the database. We will use it in the illustration of
# how to use the @transaction.atomic annotation on a view which will call this method, making
# it a part of the same transaction boundary.
def save_a_book():
    Topping.objects.create(ingredient=str(timezone.now()), perishable_date=timezone.now())


# In this example, we illustrate how you can apply the @transaction.atomic as a decorator and
# as a context manager. We will capture the current count of Pizzas, Toppings and Books, and then
# we will do the following:
#
# 1) Save a pizza.
# 2) Create an context manager
#   2.1) Save a book
#   2.2) Raise a mock exception to rollback
# 3) Save a topping
#
# Then take snapshot counts again of Pizza, Topping and Book.
# This would mean that Pizza and Topping are incremented by 1, but not book because it was rolled back.
#
# http://localhost:8000/polls/transactions/atomic
@transaction.atomic
def transaction_atomic_view(request):
    before_pizza_count = Pizza.objects.count()
    before_topping_count = Topping.objects.count()
    before_book_count = Book.objects.count()

    save_a_pizza()

    try:
        with transaction.atomic():
            save_a_book()
            raise MockRollbackError  # force rollback on book
    except MockRollbackError:
        pass # We don't do anything here

    save_a_topping()

    after_book_count = Book.objects.count()
    after_pizza_count = Pizza.objects.count()
    after_topping_count = Topping.objects.count()

    return render(request, "polls/transaction_atomic_results.html",
                  {
                      "before_pizza_count": before_pizza_count,
                      "before_topping_count": before_topping_count,
                      "before_book_count": before_book_count,
                      "after_pizza_count": after_pizza_count,
                      "after_topping_count": after_topping_count,
                      "after_book_count": after_book_count,
                  })
