from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from .models import Player, STATUS, POSITION

class PlayerForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię', widget=forms.TextInput
        (attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Nazwisko', widget=forms.TextInput
        (attrs={'class': 'form-control'}))
    year_of_birth = forms.IntegerField(label='Rocznik',
         widget=forms.NumberInput(attrs={'class': 'form-control'}))
    mail = forms.EmailField\
        (label='e-mail', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    phone = forms.IntegerField\
        (label='Numer telefonu', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    club = forms.CharField(label='Klub', widget=forms.TextInput(attrs={'class': 'form-control'}))
    position = forms.ChoiceField(choices=POSITION, label='Pozycja',
         widget=forms.Select(attrs={'class': 'form-control'}))
    status = forms.ChoiceField(choices=STATUS, label='Status', widget=forms.Select(attrs={'class': 'form-control'}))
    agent = forms.CharField(label='Kontakt do agenta/piłkarza',
                            widget=forms.Textarea(attrs={'class': 'form-control'}))
    other1 = forms.CharField(label='Uwagi',
                            widget=forms.Textarea(attrs={'class': 'form-control'}))
    other2 = forms.CharField(label='Uwagi',
                            widget=forms.Textarea(attrs={'class': 'form-control'}))
    other3 = forms.CharField(label='Uwagi',
                            widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Player
        fields = '__all__'
