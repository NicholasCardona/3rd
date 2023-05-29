from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Student

# Create your views here.


def article(request):
    return render(request, 'articles.html')


def home(request):
    names = Student.objects.all()
    return render(request, 'home.html', {'names':names})

def index(request):
    return render(request, 'index.html')







#def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

#def article_list(request):
#     articles = Article.objects.all().order_by('date')
#     return render(request, 'articles_list.html', {'article':articles})