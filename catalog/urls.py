from django.conf.urls import url, include
from catalog import views

urlpatterns = [
    url(r'^$', views.indexCatalog),
    url(r'confirm/', views.confirm, name='confirm'),
    #url(r'/carsingle', views.carsingle),
    url(r'^(?P<id>\d+)/$',
       views.carsingle,
       name='carsingle'),
]