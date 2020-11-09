from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile
#from .models import Passport

#class ProfileAdmin(admin.ModelAdmin):
    #list_display = ['user', 'user_id', 'patronymic', 'experience', 'driver_license', 'phone', 'address', 'date_of_birth']
class UserInline(admin.StackedInline):
    model = Profile # and Passport
    can_delete = False
    verbose_name_plural = 'Анкета'

class UserAdmin(UserAdmin):
    inlines = (UserInline, )
 
# Перерегистрируем модель User
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

#admin.site.register(Profile, ProfileAdmin)