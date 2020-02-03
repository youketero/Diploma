import q as q
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
from django.views.generic import ListView
from django.contrib.postgres.search import SearchVector
from django.views import View

from web.models import Articles, future_conference_anonce, entrance_specialization_way, \
    partner, type_foto, foto_article, foto_gallery, stucture_cathed, library_book, structure_person, edu_plan, \
    entrance_subject
from photologue.models import *

def home(request):
    articles = Articles.objects.order_by('id').reverse()[:8]
    foto_galery = Gallery.objects.all()
    partners = partner.objects.all()
    future_conference_anonce_full = future_conference_anonce.objects.all()
    sub = entrance_specialization_way.objects.all()
    return render(request, 'web/home.html', locals())

def vstup(request):
    sub = entrance_specialization_way.objects.all()
    return render(request, "web/vstup.html", locals())

def vstup_info(request,id):
    vs = get_object_or_404(entrance_specialization_way, code_id__specialization_id__specialization_name = id)
    #sub = entrance_subject.objects.filter(specialization_code__specialization_id__specialization_name = id)
    sub1 = entrance_specialization_way.objects.all()
    return render(request,"web/vstup_info.html",locals())

def partneru(request):
    partner_each = partner.objects.all()
    articles = Articles.objects.order_by('id').reverse()
    return render(request, 'web/partner.html', locals())

def news(request):
    articles = Articles.objects.order_by('id').reverse()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, "web/news.html", locals())

def show_articles(request, article_title):
    article = get_object_or_404(Articles, title=article_title)
    all_article = Articles.objects.order_by('id').reverse()[:4]
    return render(request, 'web/article.html', locals())

def library(request):
    books = library_book.objects.all()
    articles = Articles.objects.order_by('id').reverse()
    return render(request, "web/library.html", locals())

def galery(request):
    gallery1  = Gallery.objects.all()
    return render(request, "web/gallery.html", locals())

def show_galery(request, header_foto):
    show_galery = Photo.objects.filter(title__startswith= header_foto)
    return render(request, 'web/galery_type.html', locals())

def anonce1(request):
    future_conference_anonce_full = future_conference_anonce.objects.all()
    return render(request,'web/anonce.html',locals())

def anonce_detail(request,anonce_id):
    anonce_details = get_object_or_404(future_conference_anonce, id = anonce_id)
    articles = Articles.objects.order_by('id').reverse()[:4]
    return render(request,'web/anonce_detail.html',locals())

def contact(request):
    return render(request, "web/contact.html", locals())


def about(request):
    return render(request, "web/about.html", locals())


def structure(request):
    cathed2 = stucture_cathed.objects.all()
    return render(request, "web/structure.html", locals())

def cathed_b(request,cathed_name):
    cathed_each = get_object_or_404(stucture_cathed, cathed_name = cathed_name)
    teacher1 = structure_person.objects.filter(cathed_id__cathed_name=cathed_name)
    return  render(request, "web/cathed.html", locals())

def info(request):
    articles = Articles.objects.order_by("id").reverse()
    return render(request,"web/Information.html",locals())

def teacher(request,teacher):
    teacher = get_object_or_404(structure_person ,id = teacher)
    return render(request, "web/teacher_info.html", locals())


def edu_plans(request):
    sub = entrance_specialization_way.objects.all()
    return render(request,"web/edu_plan.html",locals())

"""




def show_articles(request, article_id):
    article = get_object_or_404(Articles, id=article_id)
    all_article = Articles.objects.all()[:4]
    return render(request, 'web/article.html', locals())

def galery(request):
    gallery1 = type_foto.objects.all()
    return render(request, "web/gallery.html", locals())

def show_galery(request, header_foto):
    show_galery1 = gallery.objects.filter(header_id__header_foto = header_foto )
    return render(request, 'web/galery_type.html', locals())

def hyper_link(request):
    return render(request, 'web/hyper_link.html', locals())

def partneru(request):
    partner_each = partner.objects.all()
    return render(request, 'web/partner.html', locals())

def cathed_b(request,cathed_name):
    cathed_each = cathed.objects.filter(cathed_name = cathed_name)
    teacher1 = teacher.objects.filter(cathed_id__cathed_name=cathed_name)
    return  render(request, "web/cathed.html", locals())

def form_user(request):
    if request.method == 'POST':
        cource = request.POST.get("cource")
        cathed = request.POST.get("cathed")
        userform = method_roz()
        roz1 = day.objects.all()
        roz = rozklad.objects.filter(cource=cource, cathed_id=cathed).order_by(
            'pare_id_id')
        return render(request, 'web/formm.html', locals())
    else:
        userform = method_roz()
        return render(request, 'web/formm.html', {"form": userform})

"""


def education(request):
    return render(request, "web/education.html",locals())


#class search(ListView):
   # model = Articles
   # template_name = 'web/search_results.html'

   # def get_queryset(self):  # новый
   #     query = self.request.GET.get('q')
   #     object_list = Articles.objects.annotate(search=SearchVector('title')).filter(search="Article")
    #    return object_list

class search(View):

    def get(self, request, *args, **kwargs):

        query = self.request.GET.get('q')
        if query is not None:
            query = self.request.GET.get('q')
            if query:
                articles = Articles.objects.annotate(search=SearchVector('title')).filter(search=query)
                partners = partner.objects.annotate(search=SearchVector('name')).filter(search=query)
                teachers = structure_person.objects.annotate(search=SearchVector('name','last_name')).filter(search=query)
        return render(request, "web/search_results.html",locals())


def handler404(request, exception, template_name="web/page404.html"):
    response = render_to_response("web/page404.html")
    response.status_code = 404
    return response