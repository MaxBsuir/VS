from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import Auto

def confirm(request):
    return render(request, 'catalog/confirm.html')


def indexCatalog(request):
    catalog = Auto.objects.all()
    return render(request, 'catalog/catalog.html', {'catalog':catalog})

def carsingle(request, id):
    cars = Auto.objects.all()
    carsingle = get_object_or_404(Auto,
                                id=id)
    return render(request, 'catalog/carsingle.html', {'catalog':cars,
                                                      'carsingle':carsingle})

#class AutosView(View):
def get(self, request):
    catalog = Auto.objects.all()
    return render(request, 'catalog/catalog.html', {'catalog':catalog})
