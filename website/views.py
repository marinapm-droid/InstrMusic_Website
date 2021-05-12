#  hello/views.py
import datetime

from django.shortcuts import render


def home_page_view(request):  # para renderizar a página home.html teremos a função home_page_view
    lista = ["Rosas", "Camomilas", "Lilás", "Túlipas"]

    context = {
        'hora': datetime.datetime.now(),
        'lista': lista,
    }
    return render(request, 'website/home.html', context)


def about_page_view(request):
    return render(request, 'website/about.html')


def contact_us_page_view(request):
    return render(request, 'website/contact_us.html')
