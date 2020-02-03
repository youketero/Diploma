from django.contrib import admin

# Register your models here.

from web.models import Articles, type_foto, entrance_code, entrance_subject, entrance_specialization, \
    entrance_specialization_way,foto_article, foto_gallery, future_conference_anonce, \
    structure_staff, stucture_cathed, structure_person, partner, library_author, library_book, edu_plan, edu_prog



class article_fil(admin.ModelAdmin):
    list_display = ["title",'date']
    list_filter = ['date']
    class Meta:
        model = Articles


admin.site.register(Articles,article_fil)
admin.site.register(type_foto)
admin.site.register(entrance_code)
admin.site.register(entrance_subject)
admin.site.register(entrance_specialization)
admin.site.register(entrance_specialization_way)

admin.site.register(foto_gallery)
admin.site.register(foto_article)
admin.site.register(future_conference_anonce)
admin.site.register(structure_staff)
admin.site.register(structure_person)


class structure_cathed_fil(admin.ModelAdmin):
    list_display = ["cathed_name"]
    class Meta:
        model = stucture_cathed
admin.site.register(stucture_cathed,structure_cathed_fil)
admin.site.register(library_book)
admin.site.register(library_author)
admin.site.register(partner)
admin.site.register(edu_plan)
admin.site.register(edu_prog)