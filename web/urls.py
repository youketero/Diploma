from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import logout

import web.views

urlpatterns = [
    url(r'^$', web.views.home, name="home"),
    url(r'^vstup/$', web.views.vstup, name="vstup"),
    url(r'^vstup/(?P<id>.*)/$', web.views.vstup_info, name="vstup_info"),
    url(r'^about/$', web.views.about, name="about"),
    url(r'^article/(?P<article_title>.*)/$', web.views.show_articles, name='article'),
    url(r'^anonce/$', web.views.anonce1, name="anonce"),
    url(r'^anonce/(?P<anonce_id>.*)/$', web.views.anonce_detail, name='anonce_detail'),
    url(r'^structure/$', web.views.structure, name='cathed'),
    url(r'^library/$', web.views.library, name="library"),
    url(r'^news/$', web.views.news, name="news"),
    url(r'^galery/$', web.views.galery, name='galery'),
    url(r'^galery/(?P<header_foto>.*)/$', web.views.show_galery, name="foto_gallery"),
    url(r'^partner/$', web.views.partneru, name="partner"),
    url(r'^contact/$', web.views.contact, name="contact"),
    url(r'^structure/(?P<cathed_name>.*)/$', web.views.cathed_b, name='cathed_name'),
    url(r'^info/$', web.views.info, name="info"),
    url(r'^teacher/(?P<teacher>.*)/$', web.views.teacher, name="teacher"),
    url(r'^edu_plan/$', web.views.edu_plans, name="edu_plan"),
    url(r'^education/$', web.views.education, name='education'),
    url(r'^search_result/$', web.views.search.as_view(), name="search"),
    url(r'^science_learning/$', web.views.science_learning, name="science_learning"),
    url(r'^phd_learning/$', web.views.phd_learning, name="phd_learning"),
    url(r'^info_for_students/$', web.views.info_for_students, name="info_for_students"),
    url(r'^info_for_students_detailed/(?P<info_title>.*)/$', web.views.info_detailed, name="info_for_students_detailed"),
    url(r'^gis_page/$',web.views.Gis_page, name="gis"),
    url(r'^cities/$',web.views.gis_city,name="cities"),
    url(r'^points/$',web.views.gis_points,name="points"),
    url(r'^geol/$',web.views.geol,name="geol"),
    url(r'^gis_page1/$',web.views.Gis_page1,name="gis1"),
]
