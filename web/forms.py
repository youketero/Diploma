from django import forms

choise_cath = (('geophysics','geophysics'),('geoinformatics','geoinformatic'),('geology','geolog'))
choise_coucre = ((1,'1'),(2,'2'),(3,'3'))

class method_roz(forms.Form):
    cathed = forms.ChoiceField(choices= choise_cath,widget=forms.Select(attrs={'class': 'form-control'}))
    cource = forms.ChoiceField(choices= choise_coucre, widget=forms.Select(attrs={'class': 'form-control'}))