from django import forms

class HoroscopeDatesForm(forms.Form):
    day = forms.IntegerField(label = 'day', min_value=1, max_value=31)
    month = forms.IntegerField(label = 'month', min_value=1, max_value=12)