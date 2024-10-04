from django import forms
from . models import Chaivarity


class Chaivarityform(forms.Form):
     chai_varity=forms.ModelChoiceField(queryset)