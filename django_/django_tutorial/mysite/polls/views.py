from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
import logging
from django.contrib.auth import authenticate, login

from .models import Question, Choice

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
        return render(request, "polls/detail.html", {'question':question, 'error_message':"You didn't select a choice!"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))

