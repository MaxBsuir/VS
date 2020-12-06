from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from catalog.models import Auto

# Create your views here.

def index (request):
    index = Auto.objects.all()
    return render(request, 'main/index.html', {'index':index})


#def carsingle(request, id):
#    cars = Auto.objects.all()
#    carsingle = get_object_or_404(Auto,
#                                id=id)
#    return render(request, 'catalog/carsingle.html', {'catalog':cars,
#                                                      'carsingle':carsingle})