from django import forms
from tempus_dominus.widgets import DateTimePicker
from django.contrib.auth import get_user_model
from Box.models import Player, STATUS, POSITION, OBSERV, POINTS, \
    ObservationForm, Comments, ObservationList


class PlayerForm(forms.ModelForm):
    first_name = forms.CharField(label='Imię', widget=forms.TextInput
    (attrs={'class': 'form', 'placeholder': 'Imię'}))
    last_name = forms.CharField(label='Nazwisko', widget=forms.TextInput
    (attrs={'class': 'form', 'placeholder': 'Nazwisko'}))
    year_of_birth = forms.IntegerField(min_value=1900, max_value=2050, label='Rocznik',
                                       widget=forms.NumberInput(attrs={'class': 'form', 'placeholder': 'Rocznik'}))
    club = forms.CharField(label='Klub', widget=forms.TextInput(attrs={'class': 'form', 'placeholder': 'Klub'}))
    position = forms.ChoiceField(choices=POSITION, label='Pozycja',
                                 widget=forms.Select(attrs={'class': 'form', 'placeholder': 'Pozycja'}))
    status = forms.ChoiceField(choices=STATUS, label='Status', widget=forms.Select(attrs={'class': 'form', 'placeholder': 'Status'}))
    mail = forms.EmailField \
        (required=False, label='e-mail', widget=forms.EmailInput(attrs={'class': 'form', 'placeholder': 'e-mail'}))
    phone = forms.IntegerField \
        (required=False, label='Numer telefonu', widget=forms.NumberInput(attrs={'class': 'form', 'placeholder': 'Numer telefonu'}))
    agent = forms.CharField(required=False, label='Kontakt do agenta',
                            widget=forms.Textarea(attrs={'class': 'form', 'placeholder': 'Kontakt do agenta'}))

    class Meta:
        model = Player
        fields = '__all__'


class ObservationFormForm(forms.ModelForm):
    # scout = forms.ModelChoiceField(queryset=get_user_model().objects.all(), label='Scout',
    #      widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    player = forms.ModelChoiceField(queryset=Player.objects.all(), label='Piłkarz',
                                    widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    observation = forms.ChoiceField(choices=OBSERV, label='Rodzaj obserwacji',
                                    widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    first_desc = forms.CharField(label='Gra w ofensywie',
                                 widget=forms.Textarea(attrs={'class': 'form', 'placeholder': ''}))
    second_desc = forms.CharField(label='Gra w defensywie',
                                  widget=forms.Textarea(attrs={'class': 'form', 'placeholder': ''}))
    third_desc = forms.CharField(label='Gra bez piłki',
                                 widget=forms.Textarea(attrs={'class': 'form', 'placeholder': ''}))
    fourth_desc = forms.CharField(label='Cechy wolicjonalne',
                                  widget=forms.Textarea(attrs={'class': 'form', 'placeholder': ''}))
    fifth_desc = forms.CharField(label='Inne',
                                 widget=forms.Textarea(attrs={'class': 'form', 'placeholder': ''}))
    sixth_desc = forms.CharField(label='Wnioski',
                                 widget=forms.Textarea(attrs={'class': 'form', 'placeholder': ''}))
    one = forms.ChoiceField(choices=POINTS, label='Technika użytkowa',
                            widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    two = forms.ChoiceField(choices=POINTS, label='Gra słabszą nogą',
                            widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    three = forms.ChoiceField(choices=POINTS, label='Siła',
                              widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    four = forms.ChoiceField(choices=POINTS, label='Koordynacja',
                             widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    five = forms.ChoiceField(choices=POINTS, label='Przyspieszenie',
                             widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    six = forms.ChoiceField(choices=POINTS, label='Agresja',
                            widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    seven = forms.ChoiceField(choices=POINTS, label='Odpowiedzialność w grze',
                              widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    eight = forms.ChoiceField(choices=POINTS, label='Skłonność do przecinania linii przeciwnika(wejściem/podaniem)',
                              widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    nine = forms.ChoiceField(choices=POINTS, label='Pracowitość',
                             widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    ten = forms.ChoiceField(choices=POINTS, label='Odbiór piłki',
                            widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))
    eleven = forms.ChoiceField(choices=POINTS, label='Gra w powietrzu',
                               widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))

    class Meta:
        model = ObservationForm
        exclude = ['scout']


class Calendar(forms.ModelForm):
    date = forms.DateTimeField(input_formats=['%Y/%m/%d %H:%M'],
                               widget=forms.widgets.DateTimeInput(attrs={'id': 'datetimepicker', 'type': 'datetime', 'class': 'form', 'placeholder': 'Data'}))
    match = forms.CharField(label='Mecz', widget=forms.TextInput(attrs={'class': 'form', 'placeholder': 'Mecz'}))
    city = forms.CharField(label='Miasto', widget=forms.TextInput
    (attrs={'class': 'form', 'placeholder': 'Miasto'}))
    country = forms.CharField(label='Kraj', initial='Polska', widget=forms.TextInput
    (attrs={'class': 'form'}))

    # scout = forms.ModelChoiceField(queryset=get_user_model().objects.all(), label='Scout',
    #      widget=forms.Select(attrs={'class': 'form', 'placeholder': ''}))

    class Meta:
        model = ObservationList
        exclude = ['scout']


class CommentsForm(forms.ModelForm):
    comment = forms.CharField(required=False, widget=forms.Textarea(attrs={'class': 'form', 'placeholder': ''}))

    class Meta:
        model = Comments
        exclude = ['player', 'date']
