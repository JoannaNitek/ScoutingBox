from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import auth_logout
from django.template.response import TemplateResponse
from django.views import View
from Users.forms import AuthenticationFormWithInactiveUsersOkay
from django.contrib.auth.views import redirect_to_login, LoginView


class LogIn(View):


    def get(self, request):
        if not request.user.is_anonymous:
            return HttpResponseRedirect('/ScoutingBox/')
        return TemplateResponse(request, 'login.html')

    def post(self, request, *args, **kwargs):

        """

        odwierziny strony z przesłanymi informacjami logowania w formularzu

        """

        if not request.user.is_anonymous:
            return HttpResponseRedirect('/ScoutingBox/')

        data = request.POST
        print(request.POST)
        user = authenticate(username=data['email'], password=data['passwd'])

        if user is not None:
            login(request, user)

            return HttpResponseRedirect('/ScoutingBox/')

        print("nueprawidlowe haslo")
        return render(request, 'login.html')

class LogOut(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/login/')
