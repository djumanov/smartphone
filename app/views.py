from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.
def home(request: HttpRequest):
    home_date = {
        'site_name': 'Smart Phone',
    }
    return render(request=request, template_name='home.html', context=home_date)