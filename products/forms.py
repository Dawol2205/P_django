from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    hashtags = forms.CharField(required=False, help_text='쉼표로 구분하여 입력해주세요')
    
    class Meta:
        model = Product
        fields = ['title', 'content', 'price', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }
