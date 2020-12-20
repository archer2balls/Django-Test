from django.urls import path
from . import views

urlpatterns = [
    # eg: /polls/
    path('', views.index, name='index'),
    # eg: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # eg: /polls/5/results
    path('<int:question_id>/results', views.results, name='results'),
    # eg: /polls/5/vote
    path('<int:question_id>/vote', views.vote, name='vote'),
    path('members/', views.members, name='members'),

]