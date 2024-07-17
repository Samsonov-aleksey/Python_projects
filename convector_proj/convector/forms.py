from django import forms


class FormConvector(forms.Form):
    amount = forms.FloatField(label='Amount')
    from_currency = forms.ChoiceField(choices=[], label='From Currency')
    to_currency = forms.ChoiceField(choices=[], label='To Currency')
