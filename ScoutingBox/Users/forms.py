from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from Box.models import Player, STATUS, POSITION, OBSERV, POINTS, ObservationForm
from Users.models import UserData

class LogInForm(forms.ModelForm):

    class Meta:
        model = UserData
        fields = '__all__'

from django.contrib.auth.forms import AuthenticationForm

class AuthenticationFormWithInactiveUsersOkay(AuthenticationForm):
    def confirm_login_allowed(self, user):
        pass