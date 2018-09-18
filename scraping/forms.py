from django import forms
from .models import Article

class url_forms(forms.ModelForm):
    class Meta:
        model=Article
        fields=('title','url',)