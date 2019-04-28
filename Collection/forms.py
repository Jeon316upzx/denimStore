from django import forms
from .models import Products

class productform(forms.ModelForm):

    MYCOLORS = (
     ('green', 'GREEN'),
     ('red', 'RED'),
     ('black', 'BLACK'),
     ('blue', 'BLUE'),
    )

    MYSIZES = (
     ('small', 'SMALL'),
     ('large', 'LARGE'),
     ('extra-large', 'E-LARGE'),
    )

    sizes = forms.ChoiceField(label='Sizes', choices=MYSIZES, widget=forms.Select(attrs={'class': "form-control"}))
    colors = forms.ChoiceField(label='Color', choices=MYCOLORS, widget=forms.Select(attrs={'class': "form-control"}))
    class Meta:
        model = Products
        fields =['sizes','colors']
