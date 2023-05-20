from .models import URL
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class URLForm(ModelForm):
    class Meta:
        model = URL
        fields = ['full_url']

        widgets = {
            "full_url": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ссылку'
            })
        }
