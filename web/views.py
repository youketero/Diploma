from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from web.models import Articles,rozklad,day
from web.forms import method_roz

def home(request):
    articles = Articles.objects.all()
    return render(request, 'web/home.html',locals())

def rozkladd(request):
    roz= rozklad.objects.all()
    return render(request,'web/rozklad.html',locals())

def about(request):
    return render(request,"web/about.html", locals())

def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    return render(request, 'web/article.html', locals())

def form_user(request):
    if request.method == 'POST':
        cource = request.POST.get("cource")
        cathed = request.POST.get("cathed")
        userform = method_roz()
        roz1 = day.objects.all()
        roz = rozklad.objects.filter(cource_id__cource_id=cource, cource_id__cathed_name=cathed).order_by('pare_id_id')
        return render(request, 'web/formm.html', locals() )
    else:
        userform = method_roz()
        return render(request,'web/formm.html',{"form":userform})

