from django import forms
from .models import Human
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов',
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm (UserCreationForm):
    username = forms.CharField(label='Имя пользователя', help_text='Максимум 150 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='E-mail', help_text='Максимум 150 символов', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Пароль для подтверждения', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')



class HumansForm(forms.ModelForm):
    # Name = forms.CharField(max_length=10, label='Имя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Surname = forms.CharField(max_length=20, label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-control'}))
    # Gender = forms.CharField(max_length=1, label='Пол', required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # profession = forms.ModelChoiceField(queryset=Profession.objects.all(), label='Профессия', empty_label="Выберите професссию", widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_name(self):
        name = self.cleaned_data['Name']
        if re.match(r'\d', name):
            raise ValueError("Имя не должно начинаться с цифры")
        return name

    class Meta:
        model = Human
        fields = ['Name', 'Surname', 'Gender', 'Date_of_birth', 'profession']
        widgets = {
            'Name': forms.TextInput(attrs={'class': 'form-control'}),
            'Surname': forms.TextInput(attrs={'class': 'form-control'}),
            'Gender': forms.TextInput(attrs={'class': 'form-control'}),
            'profession': forms.Select(attrs={'class': 'form-control'}),
            'Date_of_birth': forms.DateInput(attrs={'class': 'form-control'})
        }
