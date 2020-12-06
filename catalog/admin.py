from django.contrib import admin

from .models import Auto, Service, Road_Accident

class AutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'condition', 'body_type', 'consumption_per_100', 'price_per_day', 'fuel', 'transmission', 'power', 'reserve', 'places', 'capacity', 'engine', 'date_of_issue', 'color', 'number', 'foto']
    list_display_links = ['id', 'brand', 'model']
    list_filter = ['condition', 'brand', 'body_type', 'transmission', 'fuel', 'places']
    list_per_page = 10
    list_editable = ['condition', 'price_per_day']
    search_fields = ['brand', 'model', 'body_type', 'number']    
admin.site.register(Auto, AutoAdmin)

class Road_AccidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_auto', 'date_road_accident', 'defect']
    list_editable = ['defect']
    list_per_page = 10
    search_fields = ['date_road_accident']
admin.site.register(Road_Accident, Road_AccidentAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_road_accident', 'id_auto', 'date_of_start', 'date_of_end', 'repair_description']
    list_editable = ['repair_description']
    list_per_page = 10
    search_fields = ['date_of_start']
admin.site.register(Service, ServiceAdmin)