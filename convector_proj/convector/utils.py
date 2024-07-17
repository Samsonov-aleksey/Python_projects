import requests

def get_currency_rates(request):
    responce = requests.get(url='https://v6.exchangerate-api.com/v6/0e43e8c73e9958dfc22caa03/latest/USD').json()
    currencies = responce.get('conversion_rates')
    return currencies