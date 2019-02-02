from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from web.models import Articles


def home(request):
    articles = Articles.objects.all()
    return render(request, 'web/home.html',locals())

def rozklad(request):
    return (request,'web/rozklad.hml',locals())

def about(request):
    return render(request,"web/about.html", locals())

def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'web/article.html', locals())