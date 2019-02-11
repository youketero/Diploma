from django.contrib import admin

# Register your models here.
from web.models import Articles,rozklad, pare, subject,day,cource,teacher

class article_fil(admin.ModelAdmin):
    list_display = ["title",'date']
    list_filter = ['date']
    class Meta:
        model = Articles
class rozklad_fil(admin.ModelAdmin):
    list_display = ['pare_id_id','day_id','cource_id','subject_id']
    list_filter = ['day_id','pare_id','cource_id']
    class Meta:
        model = rozklad




admin.site.register(Articles,article_fil)
admin.site.register(rozklad,rozklad_fil)
admin.site.register(pare)
admin.site.register(day)
admin.site.register(cource)
admin.site.register(teacher)
admin.site.register(subject)