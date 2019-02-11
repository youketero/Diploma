from django.conf.urls import url

import web.views

urlpatterns = [
    url(r'^$', web.views.home, name="home"),
    url(r'^about/$', web.views.about, name ="about"),
    url(r'^article/(?P<article_id>[0-9]+)/$', web.views.show_articles, name='article'),
    url(r'^rozklad/$', web.views.rozkladd, name ="rozklad")
]

