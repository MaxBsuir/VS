from django.contrib import admin

from .models import Client, Passport, Account

class ClientAdmin(admin.ModelAdmin):
    list_display = ['id', 'surname', 'name', 'patronymic', 'phone', 'address', 'experience', 'driver_license']
    list_filter = ['experience']
    list_editable = ['phone', 'address', 'experience']
    search_fields = ['surname', 'name', 'driver_license', 'phone']    
admin.site.register(Client, ClientAdmin)
class PassportAdmin(admin.ModelAdmin):
    list_display = ['client', 'series', 'identification_number']
    search_fields = ['series', 'identification_number']    
admin.site.register(Passport, PassportAdmin)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['id_client', 'email']
    search_fields = ['id_client', 'email']    
admin.site.register(Account, AccountAdmin)