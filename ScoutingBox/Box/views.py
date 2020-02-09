import math
from collections import defaultdict

from django.urls import reverse
from django.utils import timezone
from django.shortcuts import render, redirect, get_object_or_404, render_to_response, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from datetime import datetime

from django.views.generic import UpdateView

from .forms import PlayerForm, ObservationFormForm, CommentsForm, Calendar
from .models import Player, Comments, POINTS, ObservationForm, ObservationList
import users.models


# Create your views here.


class LandingPageView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'

    def get(self, request):
        players = Player.objects.filter(status=4)
        scout = users.models.CustomUser.objects.all()
        observ = ObservationForm.objects.count()
        # forward = ObservationList.objects.filter(date__gte=datetime.today()).order_by('date')
        commm = Comments.objects.all().order_by('date')
        comm = commm.reverse()[:3]
        last = Player.objects.last()
        all = Player.objects.all()

        k = []
        b = 0
        for i in ObservationForm.objects.all():
            b = i.player
            if b not in k:
                k.append(b)
        # print(k)
        f = {}
        for i in k:
            p = i.observationform_set.all()
            s = []
            for x in p:
                s.append(x.total)
                f[x.player] = float(sum(s))

        xyz = max(zip(f.values(), f.keys()))
        print(xyz)

        context = {'players': players,
                   'observ': observ,
                   'all': all,
                   'last': last,
                   'comm': comm,
                   'scout': scout,
                   'f': f,
                   'xyz': xyz
                   }

        return render(request, 'landing-page.html', context)


class PlayerListView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        players = Player.objects.all().order_by('last_name')
        com = Comments.objects.all()
        return render(request, 'player-list-view.html', {'players': players, 'com': com})


class AddPlayerView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        form = PlayerForm()
        # form2 = CommentsForm()
        return render(request, 'add-player.html', {'form': form})

    def post(self, request):
        form = PlayerForm(request.POST)
        # form2 = CommentsForm(request.POST)
        if form.is_valid():
            new_player = form.save(commit=False)
            new_player.save()
            player_id = new_player.id
            # if form2.is_valid() and form2 is not None:
            #     new_comm = form2.save(commit=False)
            #     new_comm.player = new_player
            #     new_comm.save()

            return redirect('/player/{}'.format(player_id))
        else:
            return render(request, 'add-player.html', {'form': form})


class PlayerView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        players = Player.objects.all()
        observ = player.observationform_set.all()
        com = player.comments_set.all()
        k = []
        for i in observ:
            k.append(i.total)
        b = sum(k)

        if observ:
            s1 = int(sum([one.one for one in observ]) / len(observ) * 25)
            s2 = int(sum([two.two for two in observ]) / len(observ) * 25)
            s3 = int(sum([three.three for three in observ]) / len(observ) * 25)
            s4 = int(sum([four.four for four in observ]) / len(observ) * 25)
            s5 = int(sum([five.five for five in observ]) / len(observ) * 25)
            s6 = int(sum([six.six for six in observ]) / len(observ) * 25)
            s7 = int(sum([seven.seven for seven in observ]) / len(observ) * 25)
            s8 = int(sum([eight.eight for eight in observ]) / len(observ) * 25)
            s9 = int(sum([nine.nine for nine in observ]) / len(observ) * 25)
            s10 = int(sum([ten.ten for ten in observ]) / len(observ) * 25)
            s11 = int(sum([eleven.eleven for eleven in observ]) / len(observ) * 25)
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
            's11': s11
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
            '11a': 'Gra w powietrzu'
        }

        q = QUESTIONS

        return render(request, 'one-player.html',
                      {"q": q, 'observ': observ, 'player': player, 'com': com, 'stats': context, 'players': players,
                       'b': b})


class ComparisonView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request, play_1, play_2):
        p_1 = Player.objects.get(pk=play_1)
        p_2 = Player.objects.get(pk=play_2)
        observ1 = p_1.observationform_set.all()
        observ2 = p_2.observationform_set.all()
        count1 = observ1.count()
        count2 = observ2.count()

        if observ1:
            s1 = int(sum([one.one for one in observ1]) / len(observ1) * 25)
            s2 = int(sum([two.two for two in observ1]) / len(observ1) * 25)
            s3 = int(sum([three.three for three in observ1]) / len(observ1) * 25)
            s4 = int(sum([four.four for four in observ1]) / len(observ1) * 25)
            s5 = int(sum([five.five for five in observ1]) / len(observ1) * 25)
            s6 = int(sum([six.six for six in observ1]) / len(observ1) * 25)
            s7 = int(sum([seven.seven for seven in observ1]) / len(observ1) * 25)
            s8 = int(sum([eight.eight for eight in observ1]) / len(observ1) * 25)
            s9 = int(sum([nine.nine for nine in observ1]) / len(observ1) * 25)
            s10 = int(sum([ten.ten for ten in observ1]) / len(observ1) * 25)
            s11 = int(sum([eleven.eleven for eleven in observ1]) / len(observ1) * 25)
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

        context1 = {
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

        if observ2:
            s1 = int(sum([one.one for one in observ2]) / len(observ2) * 25)
            s2 = int(sum([two.two for two in observ2]) / len(observ2) * 25)
            s3 = int(sum([three.three for three in observ2]) / len(observ2) * 25)
            s4 = int(sum([four.four for four in observ2]) / len(observ2) * 25)
            s5 = int(sum([five.five for five in observ2]) / len(observ2) * 25)
            s6 = int(sum([six.six for six in observ2]) / len(observ2) * 25)
            s7 = int(sum([seven.seven for seven in observ2]) / len(observ2) * 25)
            s8 = int(sum([eight.eight for eight in observ2]) / len(observ2) * 25)
            s9 = int(sum([nine.nine for nine in observ2]) / len(observ2) * 25)
            s10 = int(sum([ten.ten for ten in observ2]) / len(observ2) * 25)
            s11 = int(sum([eleven.eleven for eleven in observ2]) / len(observ2) * 25)
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

        context2 = {
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

        return render(request, 'comparison.html',
                      {'p_1': p_1, 'p_2': p_2, 'observ1': observ1, 'observ2': observ2, 'q': q, 'context1': context1,
                       'context2': context2, 'count2': count2, 'count1': count1})


class PlayerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    model = Player
    form_class = PlayerForm
    template_name = 'edit-player.html'

    def get_success_url(self):
        return reverse('player', kwargs={'player_id': self.kwargs['pk']})


class PlayerDeleteView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        return render(request, 'delete-player.html', {'player': player})

    def post(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        player.delete()
        return redirect('/players/')


class ObservationFormView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
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
            new_form = form.save(commit=False)
            new_form.scout = request.user
            new_form.save()
            return redirect('/player/{}'.format(new_form.player.id))
        else:
            return render(request, 'form.html', {'form': form})


class ObservationFormPlayerView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        initial = {'player': player}
        form = ObservationFormForm(initial={'player': player})

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
        return render(request, 'form-player.html', {'form': form, 'q': q, 'p': p, 'player': player, 'initial': initial})

    def post(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        form = ObservationFormForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.scout = request.user
            new_form.save()
            return redirect('/player/{}'.format(new_form.player.id))
        else:
            return render(request, 'form-player.html', {'form': form, 'player': player})


class CalendarList(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        calendar = ObservationList.objects.filter(date__lte=timezone.now())
        forward = ObservationList.objects.filter(date__gte=timezone.now()).order_by('date')

        return render(request, 'calendar-list.html', {'calendar': calendar, 'forward': forward})


class CalendarAdd(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request):
        form = Calendar()
        return render(request, 'calendar-add.html', {'form': form})

    def post(self, request):
        form = Calendar(request.POST)
        if form.is_valid():
            new_observation = form.save(commit=False)
            new_observation.scout = request.user
            new_observation.save()
            return redirect('/calendar')
        else:
            return render(request, 'calendar-add.html', {'form': form})


class CalendarDeleteView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request, id):
        calendar = ObservationList.objects.get(pk=id)
        return render(request, '', {'calendar': calendar})

    def post(self, request):
        calendar = ObservationList.objects.get(pk=id)
        calendar.delete()
        return redirect('/calendar/')


class AddCommentFormView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request, player_id):
        form = CommentsForm()
        player = Player.objects.get(pk=player_id)
        return render(request, 'comment_add.html', {'form': form, 'player': player})

    def post(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        form = CommentsForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.player = player
            new_comment.save()
            return redirect('/player/{}'.format(player_id))
        else:
            return render(request, 'comment_add.html', {'form': form, 'player': player})


class CommentDeleteView(LoginRequiredMixin, View):
    login_url = '/accounts/login/'
    redirect_field_name = '/login/'

    def get(self, request, com_id, player_id):
        player = Player.objects.get(pk=player_id)
        comm = Comments.objects.get(pk=com_id)
        return render(request, 'delete-comment.html', {'player': player, 'comm': comm})

    def post(self, request, com_id, player_id):
        player = Player.objects.get(pk=player_id)
        comm = Comments.objects.get(pk=com_id)
        comm.delete()
        return redirect('/player/{}'.format(player.id))
