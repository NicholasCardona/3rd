from django.contrib import admin
from django.urls import path
from . import views




app_name = 'Articles'


urlpatterns = [
    path("", views.home, name='home'),
    path('articles/<slug>', views.article_details, name = 'articles'),
    path('index/', views.index, name ='index'),
    path('create/', views.create, name='create'),
    path('members/<name>', views.members, name='members'),
    path('drivers/', views.drivers, name='drivers')
    



    # path("results/<int:question_id>/", views.results, name="results"),
    # path('testing/<int:numbering>', views.testing, name = 'testing'),
]

    



