from django.conf.urls import url, include

from . import views

app_name = 'polls'
urlpatterns = [
    url('^signin', views.signin, name='signin'),
    # example: /polls/
    url(r'^$', views.landing, name='landing'),
    # example: /polls/dashboard
    url(r'^dashboard/$', views.IndexView.as_view(), name='dashboard'),
    # example: /polls/5/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # example: /polls/5/results
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    # example: /polls/5/vote
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]
