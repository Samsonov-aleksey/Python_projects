from django.shortcuts import render, get_object_or_404,redirect
from django.views.generic import ListView,DetailView
from django.views.generic.base import TemplateView
from .forms import HoroscopeDatesForm
from .models import Horoscope, Elem
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotFound

def list_elem(request, pk):
    elem = get_object_or_404(Elem, pk=pk)
    signs = Horoscope.objects.filter(elem=elem)
    return render(request, 'horoscope/detail_elem.html', {'elem': elem, 'signs': signs})

class ListHoroscope(ListView):
    template_name = 'horoscope/horoscope.html'
    context_object_name = 'signs'
    model = Horoscope

class ListElems(ListView):
    model = Elem
    template_name = 'horoscope/elems.html'
    context_object_name = 'elems'

class DetailSign(DetailView):
    template_name = 'horoscope/detail_sign.html'
    model = Horoscope

class ListElem(ListView):
    template_name = 'horoscope/detail_elem.html'
    model = Horoscope
    context_object_name = 'signs'

class DoneView(TemplateView):
    template_name ='horoscope/index.html'

def month_day_to_sign_zodiac(request):
    form = HoroscopeDatesForm()
    if request.method == 'POST':
        form = HoroscopeDatesForm(request.POST)
        if form.is_valid():
            day = form.cleaned_data['day']
            month = form.cleaned_data['month']
            year = datetime.now().year
            try:
                date_obj = datetime(year, month, day)
            except ValueError:
                return render(request, 'horoscope/horoscope_dates_form.html', {'form': form})
            if (datetime(year, 1, 1) <= date_obj <= datetime(year,1,20)) or (datetime(year, 12, 23) <= date_obj <= datetime(year,12,31)):
                return redirect(f'/horoscope/6/')
            for obj in Horoscope.objects.all():
                if obj.get_begin_date() <= date_obj <= obj.get_end_date():
                    return redirect(f'/horoscope/{obj.id}/')
    return render(request, 'horoscope/horoscope_dates_form.html', {'form': form})