from django.shortcuts import render
import requests

def map_page(request):
    data = {'data': 'text'}
    return render(request, 'index.html', data)
