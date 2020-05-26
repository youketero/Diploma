from django.contrib import admin

# Register your models here.
from leaflet.admin import LeafletGeoAdmin
from web.models import Articles, type_foto, entrance_code, entrance_subject, entrance_specialization, \
    entrance_specialization_way, foto_article, foto_gallery, future_conference_anonce, \
    structure_staff, stucture_cathed, structure_person, partner, library_author, library_book, edu_plan, edu_prog, Info, \
    pointX, Points, Points_city, shape_loader, Geology, geol_raster


class article_fil(admin.ModelAdmin):
    list_display = ["title", 'date']
    list_filter = ['date']

    class Meta:
        model = Articles


admin.site.register(Articles, article_fil)

admin.site.register(type_foto)
admin.site.register(entrance_code)
admin.site.register(entrance_subject)
admin.site.register(entrance_specialization)
admin.site.register(entrance_specialization_way)
admin.site.register(shape_loader)
class PointX(LeafletGeoAdmin):
    list_display = ["pointX"]

admin.site.register(pointX,LeafletGeoAdmin)

class points(LeafletGeoAdmin):
    list_display = ["point_numb"]

admin.site.register(Points,points)

class geol(LeafletGeoAdmin):
    list_display = ["gen_glg"]

admin.site.register(Geology,geol)


class points1(LeafletGeoAdmin):
    list_display = ["city_name"]

admin.site.register(Points_city,points1)


class raster(LeafletGeoAdmin):
    list_display = ["name"]

admin.site.register(geol_raster,raster)

admin.site.register(foto_gallery)
admin.site.register(foto_article)
admin.site.register(future_conference_anonce)
admin.site.register(structure_staff)

class structure_person_fil(admin.ModelAdmin):
    list_display = ["name","last_name"]

    class Meta:
        model = structure_person

admin.site.register(structure_person,structure_person_fil)


class structure_cathed_fil(admin.ModelAdmin):
    list_display = ["cathed_name"]

    class Meta:
        model = stucture_cathed


admin.site.register(stucture_cathed, structure_cathed_fil)
admin.site.register(library_book)
admin.site.register(library_author)
admin.site.register(partner)
admin.site.register(edu_plan)
admin.site.register(edu_prog)
admin.site.register(Info)
