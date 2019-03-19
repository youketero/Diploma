from django.contrib import admin

# Register your models here.
from web.models import Articles,rozklad, pare, subject,day,teacher,cathed,room,gallery,type_foto

class article_fil(admin.ModelAdmin):
    list_display = ["title",'date']
    list_filter = ['date']
    class Meta:
        model = Articles
class rozklad_fil(admin.ModelAdmin):
    list_display = ['pare_id_id','day_id','cource','subject_id']
    list_filter = ['day_id','pare_id','cource']
    class Meta:
        model = rozklad




admin.site.register(Articles,article_fil)
admin.site.register(rozklad,rozklad_fil)
admin.site.register(pare)
admin.site.register(day)
admin.site.register(teacher)
admin.site.register(subject)
admin.site.register(cathed)
admin.site.register(room)
admin.site.register(gallery)
admin.site.register(type_foto)