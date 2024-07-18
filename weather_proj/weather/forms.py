from django import forms
from django.core.exceptions import ValidationError

class FormWeather(forms.Form):
    city = forms.CharField(max_length=40)

    def clean_city(self):
        city = self.cleaned_data['city']
        if not city.isalpha():
            raise ValidationError('Название города должно содержать только буквы.')
        return city

