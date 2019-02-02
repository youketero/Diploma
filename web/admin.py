from django.contrib import admin

# Register your models here.
from web.models import Articles

class article_fil(admin.ModelAdmin):
    list_display = ["title",'date']
    list_filter = ['date']
    class Meta:
        model = Articles

admin.site.register(Articles,article_fil)