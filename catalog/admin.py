from django.contrib import admin

from .models import Auto, Service, Road_Accident

class AutoAdmin(admin.ModelAdmin):
    list_display = ['id', 'brand', 'model', 'condition', 'body_type', 'consumption_per_100', 'price_per_day', 'color', 'number', 'engine', 'transmission', 'date_of_issue']
    list_filter = ['brand', 'body_type', 'transmission', 'condition']
    list_editable = ['condition', 'price_per_day']
    search_fields = ['brand', 'model', 'body_type', 'transmission']    
admin.site.register(Auto, AutoAdmin)

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_auto', 'date_of_start', 'date_of_end', 'repair_description']
    list_editable = ['repair_description']
    search_fields = ['date_of_start']
admin.site.register(Service, ServiceAdmin)

class Road_AccidentAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_auto', 'id_service', 'date_road_accident', 'defect']
    list_editable = ['defect']
    search_fields = ['date_road_accident']
admin.site.register(Road_Accident, Road_AccidentAdmin)