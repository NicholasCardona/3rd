from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path('articles/', views.article),

    
    # ex: /polls/5/results/
    path("results/<int:question_id>/", views.results, name="results"),
    path('testing/<int:numbering>', views.testing, name = 'testing'),
    path('article1/', views.article_list )
]



