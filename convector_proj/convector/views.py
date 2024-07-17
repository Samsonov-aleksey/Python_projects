from django.shortcuts import render
import requests
from .forms import FormConvector
from django.http import HttpResponse
# Create your views here.

def exchange(request):
    responce = requests.get(url='https://v6.exchangerate-api.com/v6/0e43e8c73e9958dfc22caa03/latest/USD').json()
    currencies = responce.get('conversion_rates')
    currency_choices = [(key, key) for key in currencies.keys()]

    if request.method == 'POST':
        form = FormConvector(request.POST)
        form.fields['from_currency'].choices = currency_choices
        form.fields['to_currency'].choices = currency_choices
        if form.is_valid():
            from_currency = form.cleaned_data['from_currency']
            to_currency = form.cleaned_data['to_currency']
            amount = form.cleaned_data['amount']
            result = round(amount/(currencies[from_currency])*(currencies[to_currency]),2)
            context = {
                'from_currency': from_currency,
                'to_currency': to_currency,
                'amount': amount,
                'result': result,
            }
            return render(request, 'convector/done.html', context=context)
    else:
        form = FormConvector()
        form.fields['from_currency'].choices = currency_choices
        form.fields['to_currency'].choices = currency_choices

    context = {
        'currencies': currencies
    }
    return render(request, 'convector/index.html', context=context)

