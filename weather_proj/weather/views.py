from django.shortcuts import render
import requests
from django.http import HttpResponse
from .config import open_weather_token
from .forms import FormWeather


def weather_info(request):
    if request.method == 'POST':
        form = FormWeather(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            api_key = open_weather_token
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru"

            response = requests.get(url)
            if response.status_code == 200:
                weather_data = response.json()
                request.session['last_city'] = city
                context = {
                    'city': weather_data['name'],
                    'temperature': weather_data['main']['temp'],
                    'description': weather_data['weather'][0]['description'],
                    'wind_speed': weather_data['wind']['speed'],
                    'humidity': weather_data['main']['humidity'],
                }
                return render(request, 'weather/index.html', context=context)
            else:
                form = FormWeather()
                return render(request, 'weather/index.html', {'form': form})
        else:
            form = FormWeather()
    else:
        last_city = request.session.get('last_city', '')
        form = FormWeather(initial={'city': last_city})
    return render(request, 'weather/index.html', {'form': form})
