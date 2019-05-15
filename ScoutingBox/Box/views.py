from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.views import View
from django.views.generic import CreateView, DeleteView
from .models import Player, ObservationForm, ObservationList, OBSERV
from .forms import PlayerForm, ObservationFormForm

# Create your views here.


class LandingPageView(View):

    def get(self, request):
        return render(request, 'landing-page.html', {})


class PlayerListView(View):

    def get(self, request):
        players = Player.objects.all()
        return render(request, 'player-list-view.html', {'players': players})

class AddPlayerView(View):

    def get(self, request):

        form = PlayerForm()
        return render(request, 'add-player.html',
                      {'form': form})

    def post(self, request, player_id):
        form = PlayerForm(request.POST)
        if form.is_valid():
           new_player = form.save()
           player_id = new_player.id
           return redirect('/player/{}'.format(player_id))
        else:
            return render(request, 'add-player.html', {'form': form})

class PlayerView(View):

    def get(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        return render(request, 'one-player.html',
                      {'player_id': player_id, 'player':player})


class ObservationFormView(View):
    def get(self, request):
        form = ObservationFormForm()
        return render(request, 'form.html', {'form': form})