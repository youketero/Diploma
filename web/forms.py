from django import forms
from django.contrib.gis import forms
from web.models import Points_city, shape_loader

class DocumentForm(forms.ModelForm):
    class Meta:
        model = shape_loader
        fields = ('file',)

choise_cath = (('geophysics', 'geophysics'), ('geoinformatics', 'geoinformatic'), ('geology', 'geolog'))
choise_coucre = ((1, '1'), (2, '2'), (3, '3'))


class method_roz(forms.Form):
    cathed = forms.ChoiceField(choices=choise_cath, widget=forms.Select(attrs={'class': 'form-control'}))
    cource = forms.ChoiceField(choices=choise_coucre, widget=forms.Select(attrs={'class': 'form-control'}))


class func_score(forms.Form):
    at_score = forms.FloatField(max_value=12.0, min_value=0.0)
    first_subject = forms.IntegerField(min_value=100, max_value=200)
    second_subject = forms.IntegerField(min_value=100, max_value=200)
    third_subject = forms.IntegerField(min_value=100, max_value=200)

