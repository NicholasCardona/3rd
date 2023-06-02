from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Student, Drivers
from django.contrib.auth.decorators import login_required

# Create your views here.


def article_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles.html', {'articles': article})
    


def home(request):
    articles = Article.objects.all()
    names = Student.objects.all()
    return render(request, 'home.html',   {'names':names,'articles': articles , 'username':request.user.username})

def index(request):
    return render(request, 'index.html')


def members(request, name):
    Members = Student.objects.get(name=name)
    return render(request, 'members.html', {'members': Members})


def drivers(request):
        Drivers_list = Drivers.objects.all()
        return render(request, 'Drivers.html', {'Drivers':Drivers_list})


@login_required(login_url='Accounts:login')
def create(request):
     return render(request, 'create.html')









#def results(request, question_id):
#     response = "You're looking at the results of question %s."
#     return HttpResponse(response % question_id)

#def article_list(request):
#     articles = Article.objects.all().order_by('date')
#     return render(request, 'articles_list.html', {'article':articles})