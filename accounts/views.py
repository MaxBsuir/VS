from django.shortcuts import render
from django.contrib.auth.models import User
from django import forms
from .models import Profile
#from .models import Passport
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
#from .forms import LoginForm, UserRegistrationForm, UserEditForm, ProfileEditForm

class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(label='')
    last_name = forms.CharField(label='')
    email = forms.EmailField(label='')
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (forms.TextInput, forms.EmailInput):
                    field.widget = forms.TextInput(attrs={'class':'form-control'})
                    if field_name=='first_name':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Имя'})
                    if field_name=='last_name':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Фамилия'})
                    if field_name=='email':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Email'})
   
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    patronymic = forms.CharField(label='', max_length=50)
    phone = forms.CharField(label='', min_length=13, max_length=13)
    experience = forms.IntegerField(label='', min_value=2, max_value=49) ########## Добавить disabled=True ##########
    driver_license = forms.CharField(label='', min_length=8, max_length=8) ########## Добавить disabled=True ##########
    #date_of_birth = forms.CharField(label='', required=False)
    #address = forms.CharField(label='', required=False)
    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields.get(field_name)  
            if field:
                if type(field.widget) in (forms.TextInput, forms.EmailInput, forms.DateInput):
                    field.widget = forms.TextInput(attrs={'class':'form-control'})
                    if field_name=='patronymic':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Отчество'})
                    if field_name=='phone':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Телефон'})
                    if field_name=='experience':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Опыт вождения (лет)'})
                    if field_name=='driver_license':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': '№ лиценции'})
                    if field_name=='date_of_birth':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Дата рождения'})
                    if field_name=='address':
                        field.widget = forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Адрес'})
   
    class Meta:
        model = Profile
        #exclude = ('patronymic', 'driver_license', 'experience', 'phone', 'date_of_birth', 'address',)########################################
        fields = ('patronymic', 'driver_license', 'experience', 'phone', 'date_of_birth', 'address',)

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
           user_form.save()
           profile_form.save()
           return render(request, 'main/index.html')           
        else:
           messages.error(request, 'Введите корректные данные')
           return HttpResponse('<h1>Введите корректные данные</h1>')
           
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
        return render(request, 'accounts/edit.html', {'user_form': user_form, 'profile_form': profile_form})


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Логин'}))
    first_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Имя'}))
    last_name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Фамилия'}))
    #patronymic = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Отчество'}))
    #phone = forms.CharField(label='', min_length=13, max_length=13, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Телефон'}))
    #experience = forms.IntegerField(label='', min_value=2, max_value=49, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Опыт вождения (лет)'}))
    #driver_license = forms.CharField(label='', min_length=8, max_length=8, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder': '№ лиценции'}))
    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        #fields = ('username', 'first_name', 'last_name', 'email', 'patronymic', 'phone', 'experience', 'driver_license')
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            profile = Profile.objects.create(user=new_user)
            return render(request, 'accounts/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'user_form': user_form})