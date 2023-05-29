from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path("", views.home),
    path('articles/', views.article),

    
    path("results/<int:question_id>/", views.results, name="results"),
    path('testing/<int:numbering>', views.testing, name = 'testing'),
    path('article1/', views.article_list ),
    path('index/', views.index),
]

urlpatterns += staticfiles_urlpatterns()