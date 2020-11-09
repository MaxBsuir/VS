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
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    email = forms.EmailField(label='Email')
   
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    patronymic = forms.CharField(label='Отчество', max_length=50)
    phone = forms.CharField(label='Телефон', min_length=13, max_length=13)
    experience = forms.IntegerField(label='Опыт вождения (лет)', min_value=2, max_value=49) ########## Добавить disabled=True ##########
    driver_license = forms.CharField(label='№ лиценции', min_length=8, max_length=8) ########## Добавить disabled=True ##########
   
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
    username = forms.CharField(label='Логин', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(label='Имя', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label='Фамилия', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    patronymic = forms.CharField(label='Отчество', max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(label='Телефон', min_length=13, max_length=13, widget=forms.TextInput(attrs={'class':'form-control'}))
    experience = forms.IntegerField(label='Опыт вождения (лет)', min_value=2, max_value=49)
    driver_license = forms.CharField(label='№ лиценции', min_length=8, max_length=8, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'patronymic', 'phone', 'experience', 'driver_license')

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