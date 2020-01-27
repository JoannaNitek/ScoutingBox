# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = '__all__'


class UserCreationForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = '__all__'


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form', 'placeholder': 'email'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class': 'form', 'placeholder': 'hasło'}))

    class Meta:
        model = CustomUser
        fields = '__all__'
