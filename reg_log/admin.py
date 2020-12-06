from django.contrib import admin

from .models import Client, Employee

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'surname', 'name', 'patronymic', 'series', 'identification_number', 'phone', 'driver_license', 'experience', 'email', 'address']
    list_per_page = 10
    list_filter = ['series', 'experience']
    list_display_links = ['id', 'surname', 'name']
    search_fields = ['surname', 'name', 'patronymic', 'driver_license', 'phone', 'email', 'series', 'identification_number']    
admin.site.register(Client, ClientAdmin)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id', 'second_name', 'first_name', 'third_name', 'employment_date']
    list_per_page = 10
    list_display_links = ['id', 'first_name', 'second_name']
    search_fields = ['first_name', 'second_name', 'third_name', 'employment_date']    
admin.site.register(Employee, EmployeeAdmin)


#list_display = ['id', 'brand', 'model', 'condition', 'body_type', 'consumption_per_100', 'price_per_day', 'fuel', 'transmission', 'power', 'reserve', 'places', 'capacity', 'engine', 'date_of_issue', 'color', 'number', 'foto']
#    list_display_links = ['id', 'brand']
#    list_filter = ['condition', 'brand', 'body_type', 'transmission', 'fuel', 'places']
#    list_per_page = 10
#    list_editable = ['condition', 'price_per_day']
#    search_fields = ['brand', 'model', 'body_type', 'number']    