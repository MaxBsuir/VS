from django.shortcuts import render

def indexCatalog(request):
    return render(request, 'catalog/catalog.html')