from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView, DeleteView
from .models import Player, ObservationForm, ObservationList, OBSERV, POINTS, QUESTION
from .forms import PlayerForm, ObservationFormForm, Calendar
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class LandingPageView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        return render(request, 'landing-page.html', {})


class PlayerListView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        players = Player.objects.all()
        return render(request, 'player-list-view.html', {'players': players})

class AddPlayerView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'

    def get(self, request):

        form = PlayerForm()
        return render(request, 'add-player.html', {'form': form})

    def post(self, request):
        form = PlayerForm(request.POST)
        if form.is_valid():
           new_player = form.save()
           player_id = new_player.id
           return redirect('/player/{}'.format(player_id))
        else:
            return render(request, 'add-player.html', {'form': form})

class PlayerView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'

    def get(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        observ = player.observationform_set.all()

        if observ:
            s1 = sum([one.one for one in observ]) / len(observ)*25
            s2 = sum([two.two for two in observ]) / len(observ)*25
            s3 = sum([three.three for three in observ]) / len(observ)*25
            s4 = sum([four.four for four in observ]) / len(observ)*25
            s5 = sum([five.five for five in observ]) / len(observ)*25
            s6 = sum([six.six for six in observ]) / len(observ)*25
            s7 = sum([seven.seven for seven in observ]) / len(observ)*25
            s8 = sum([eight.eight for eight in observ]) / len(observ)*25
            s9 = sum([nine.nine for nine in observ]) / len(observ)*25
            s10 = sum([ten.ten for ten in observ]) / len(observ)*25
            s11 = sum([eleven.eleven for eleven in observ]) / len(observ)*25
        else:
            s1 = 0
            s2 = 0
            s3 = 0
            s4 = 0
            s5 = 0
            s6 = 0
            s7 = 0
            s8 = 0
            s9 = 0
            s10 = 0
            s11 = 0


        context = {
            's1': s1,
            's2': s2,
            's3': s3,
            's4': s4,
            's5': s5,
            's6': s6,
            's7': s7,
            's8': s8,
            's9': s9,
            's10': s10,
            's11': s11,
        }

        QUESTIONS = {
            '1': 'Gra w ofensywie',
            '2': 'Gra w defensywie',
            '3': 'Gra bez piłki',
            '4': 'Cechy wolicjonalne',
            '5': 'Inne',
            '6': 'Wnioski',
            '1a': 'Technika użytkowa',
            '2a': 'Gra słabszą nogą',
            '3a': 'Siła',
            '4a': 'Koordynacja',
            '5a': 'Przyspieszenie',
            '6a': 'Agresja',
            '7a': 'Odpowiedzialność w grze',
            '8a': 'Skłonność do przecinania linii przeciwnika (wejściem/ podaniem)',
            '9a': 'Pracowitość',
            '10a': 'Odbiór piłki',
            '11a': 'Gra w powietrzu'}

        q = QUESTIONS

        return render(request, 'one-player.html', {"q": q, 'observ': observ, 'player': player, 'stats': context})


class ObservationFormView(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        form = ObservationFormForm()
        QUESTIONS = {
            '1': 'Gra w ofensywie',
            '2': 'Gra w defensywie',
            '3': 'Gra bez piłki',
            '4': 'Cechy wolicjonalne',
            '5': 'Inne',
            '6': 'Wnioski',
            '1a': 'Technika użytkowa',
            '2a': 'Gra słabszą nogą',
            '3a': 'Siła',
            '4a': 'Koordynacja',
            '5a': 'Przyspieszenie',
            '6a': 'Agresja',
            '7a': 'Odpowiedzialność w grze',
            '8a': 'Skłonność do przecinania linii przeciwnika (wejściem/ podaniem)',
            '9a': 'Pracowitość',
            '10a': 'Odbiór piłki',
            '11a': 'Gra w powietrzu'}
        q = QUESTIONS
        p = POINTS
        return render(request, 'form.html', {'form': form, 'q': q, 'p': p})

    def post(self, request):
        form = ObservationFormForm(request.POST)
        if form.is_valid():
            new_form = form.save()

            return redirect('/player/{}'.format(new_form.player.id))
        else:
            return render(request, 'form.html', {'form': form})


class CalendarList(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        calendar = ObservationList.objects.all()
        return render(request, 'calendar-list.html', {'calendar': calendar})

class CalendarAdd(LoginRequiredMixin, View):
    login_url = '/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        form = Calendar()
        return render(request, 'calendar-add.html', {'form': form})


    def post(self, request):
        form = Calendar(request.POST)
        if form.is_valid():
            new_observation = form.save()
            return redirect('/calendar/')
        else:
            return render(request, 'calendar-add.html', {'form': form})

