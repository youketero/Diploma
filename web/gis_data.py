import os
from django.contrib.gis.utils import LayerMapping
from web.models import Points, Points_city, Geology

points_mapping = {
    'lat': 'LAT',
    'lon': 'LON',
    'name': 'NAME',
    'aux1': 'AUX1',
    'aux2': 'AUX2',
    'aux3': 'AUX3',
    'longname': 'LONGNAME',
    'datetime': 'DATETIME',
    'point_numb': 'point_numb',
    'dip': 'DIP',
    'dip_angle': 'DIP_angle',
    'dip_prost': 'DIP_prost',
    'rock': 'Rock',
    'point_type': 'point_type',
    'geom': 'MULTIPOINT',
}

points_city_mapping = {
    'city_name': 'CITY_NAME',
    'admin_name': 'ADMIN_NAME',
    'cntry_name': 'CNTRY_NAME',
    'status': 'STATUS',
    'geom': 'POINT',
}


geology_mapping = {
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'type': 'TYPE',
    'glg': 'GLG',
    'gen_glg': 'GEN_GLG',
    'geom': 'MULTIPOLYGON',
}


points_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"static/gis_data/points_all.shp"))
city_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"static/gis_data/Europe_National_Provinces_Capitals.shp"))
geol_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),"static/gis_data/geo3cl.shp"))



def geol(verbose=True):
    ll = LayerMapping(Geology,geol_shp,geology_mapping, transform=True,encoding="utf-8")
    ll.save(strict=True,verbose=False)

def run(verbose=True):
    lm = LayerMapping(Points,points_shp,points_mapping, transform=False,encoding="utf-8")
    lm.save(strict=True,verbose=False)

def run_city(verbose=True):
    lm = LayerMapping(Points_city,city_shp,points_city_mapping, transform=False,encoding="utf-8")
    lm.save(strict=True,verbose=False)

def run_shape(shape,verbose=True):
    city_shp1 = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "static/gis_data/"+shape+".shp"))
    lm = LayerMapping(Points_city,city_shp1,points_city_mapping, transform=False,encoding="utf-8")
    lm.save(strict=True,verbose=False)