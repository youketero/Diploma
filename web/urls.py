from django.conf.urls import url

import web.views

urlpatterns = [
    url(r'^$', web.views.home, name="home"),
    url(r'^about/$', web.views.about, name ="about"),
    url(r'^article/(?P<article_id>\w+)/$', web.views.show_articles, name='article'),
    url(r'^anonce/$', web.views.anonce1, name ="anonce"),
    url(r'^formm/$', web.views.form_user ,name='forms'),
    url(r'^structure/$', web.views.structure, name='cathed'),
    url(r'^library/$', web.views.library, name="library"),
    url(r'^news/$', web.views.news, name="news"),
    url(r'^galery/$', web.views.galery,name='galery'),
    url(r'^galery/(?P<id>\w+)/$', web.views.show_galery, name = "g"),
    url(r'^partner/$', web.views.partneru, name="partner"),
    url(r'^hyper_link/$', web.views.hyper_link, name = "usefull_link")
]

