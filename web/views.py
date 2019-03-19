from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

# Create your views here.
from web.models import Articles, rozklad, day, anonce, cathed, gallery, partner, hyper_link_usefull, type_foto
from web.forms import method_roz


def home(request):
    articles = Articles.objects.all()
    return render(request, 'web/home.html', locals())


def rozkladd(request):
    roz = rozklad.objects.all()
    return render(request, 'web/rozklad.html', locals())


def about(request):
    return render(request, "web/about.html", locals())


def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    all_article = Articles.objects.all()[:4]
    return render(request, 'web/article.html', locals())


def form_user(request):
    if request.method == 'POST':
        cource = request.POST.get("cource")
        cathed = request.POST.get("cathed")
        userform = method_roz()
        roz1 = day.objects.all()
        roz = rozklad.objects.filter(cource_id__cource_id=cource, cource_id__cathed_name__cathed_name=cathed).order_by(
            'pare_id_id')
        return render(request, 'web/formm.html', locals())
    else:
        userform = method_roz()
        return render(request, 'web/formm.html', {"form": userform})


def anonce1(request):
    anonc = anonce.objects.all()
    return render(request, "web/rozklad.html", locals())


def structure(request):
    cathed2 = cathed.objects.all()
    return render(request, "web/structure.html", locals())


def library(request):
    return render(request, "web/library.html", locals())


def news(request):
    articles = Articles.objects.all()
    return render(request, "web/news.html", locals())


def galery(request):
    gallery1 = type_foto.objects.all()
    return render(request, "web/gallery.html", locals())

def show_galery(request, id):
    show_galery1 = gallery.objects.filter(header_id = id)
    return render(request, 'web/galery_type.html', locals())

def hyper_link(request):
    return render(request, 'web/hyper_link.html', locals())

def partneru(request):
    return render(request, 'web/partner.html', locals())