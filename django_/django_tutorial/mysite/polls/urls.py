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
    # The url mappings used to illustrate how ATOMIC_REQUESTS is used.
    url(r'^transactions/atomic_request/success$', views.atomic_request_success, name='atomic_request_success'),
    url(r'^transactions/atomic_request/rollback$', views.atomic_request_rollback, name='atomic_request_rollback'),
    url(r'^transactions/atomic_request/skip$', views.atomic_request_skip, name='atomic_request_skip'),
    # The url mappings used to illustrate how @transaction.atomic is used
    url(r'^transactions/atomic', views.transaction_atomic_view, name="transaction_atomic"),
    # The url mappings used to illustrate how the transaction savepoint functions is used
    url(r'^transactions/savepoint', views.transaction_savepoint_view, name="transaction_savepoint")
]
