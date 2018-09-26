from django.conf.urls import url

import web.views

urlpatterns = [
    url(r'^$', web.views.base, name="base")]

