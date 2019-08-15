from datetime import datetime

from django.forms import formset_factory
from django.shortcuts import render, redirect, get_object_or_404, render_to_response, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from .forms import PlayerForm, ObservationFormForm, Calendar, CommentsForm
from .models import Player, ObservationList, Comments, POINTS, ObservationForm


# Create your views here.

class LandingPageView(View):
# dodaj do klasy dziedziczenie po LoginRequiredMixin
#     login_url = '/login/'

    def get(self, request):
        players = Player.objects.filter(status=4)
        forward = ObservationList.objects.filter(date__gte=datetime.today()).order_by('date')
        comm = Comments.objects.latest('date')

        return render(request, 'landing-page.html', {'players': players, 'forward': forward, 'comm': comm})


class PlayerListView(View):
    # login_url = '/login/'
    # redirect_field_name = '/login/'

    def get(self, request):
        players = Player.objects.all().order_by('last_name')
        com = Comments.objects.all()
        return render(request, 'player-list-view.html', {'players': players, 'com': com})


class AddPlayerView(View):
    # login_url = '/login/'
    # redirect_field_name = '/login/'

    def get(self, request):
        form = PlayerForm()
        form2 = CommentsForm()
        return render(request, 'add-player.html', {'form': form, 'form2': form2})

    def post(self, request):
        form = PlayerForm(request.POST)
        form2 = CommentsForm(request.POST)
        if form.is_valid() and form2.is_valid():
            new_player = form.save(commit=False)
            new_player.save()
            player_id = new_player.id

            new_comm = form2.save(commit=False)
            new_comm.player = new_player
            new_comm.save()

            return redirect('/player/{}'.format(player_id))
        else:
            return render(request, 'add-player.html', {'form': form, 'form2': form2})


class PlayerView(View):
    # login_url = '/login/'
    # redirect_field_name = '/login/'

    def get(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        observ = player.observationform_set.all()
        com = player.comments_set.all()

        if observ:
            s1 = int(sum([one.one for one in observ]) / len(observ)*25)
            s2 = int(sum([two.two for two in observ]) / len(observ)*25)
            s3 = int(sum([three.three for three in observ]) / len(observ)*25)
            s4 = int(sum([four.four for four in observ]) / len(observ)*25)
            s5 = int(sum([five.five for five in observ]) / len(observ)*25)
            s6 = int(sum([six.six for six in observ]) / len(observ)*25)
            s7 = int(sum([seven.seven for seven in observ]) / len(observ)*25)
            s8 = int(sum([eight.eight for eight in observ]) / len(observ)*25)
            s9 = int(sum([nine.nine for nine in observ]) / len(observ)*25)
            s10 = int(sum([ten.ten for ten in observ]) / len(observ)*25)
            s11 = int(sum([eleven.eleven for eleven in observ]) / len(observ)*25)
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

        return render(request, 'one-player.html', {"q": q, 'observ': observ, 'player': player, 'com': com, 'stats': context})


class PlayerEditView(View):
        # login_url = '/login/'
        # redirect_field_name = '/login/'

        def get(self, request, player_id):
            player = get_object_or_404(Player, pk=player_id)
            form = PlayerForm(instance=player)
            return render(request, 'edit-player.html', {'form': form, 'player': player})

        def post(self, request, player_id):
            player = get_object_or_404(Player, pk=player_id)
            form = PlayerForm(request.POST, instance=player)
            if form.is_valid():
                form.save()
                return redirect('/player/{}'.format(player_id))
            else:
                return render(request, 'edit-player.html', {'form': form})


class PlayerDeleteView(View):
    def get(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        return render(request, 'delete-player.html', {'player': player})

    def post(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        player.delete()
        return redirect('/players/')
# class AddPlayerView(View):
#     # login_url = '/login/'
#     # redirect_field_name = '/login/'
#
#     def get(self, request):
#         form = PlayerForm()
#         form2 = CommentsForm()
#         return render(request, 'add-player.html', {'form': form, 'form2': form2})
#
#     def post(self, request):
#         form = PlayerForm(request.POST)
#         form2 = CommentsForm(request.POST)
#         if form.is_valid() and form2.is_valid():
#             new_player = form.save(commit=False)
#             new_player.save()
#             player_id = new_player.id
#
#             new_comm = form2.save(commit=False)
#             new_comm.player = new_player
#             new_comm.save()
#
#             return redirect('/player/{}'.format(player_id))
#         else:
#             return render(request, 'add-player.html', {'form': form, 'form2': form2})


class ObservationFormView(View):
    # login_url = '/login/'
    # redirect_field_name = '/login/'

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


class ObservationFormPlayerView(View):
    # login_url = '/login/'
    # redirect_field_name = '/login/'

    def get(self, request, player_id):
        player = Player.objects.get(pk=player_id)
        initial = {'player': player}
        form = ObservationFormForm(initial={'player': player})

        # def view(request):
        #     game = Game.objects.get(id=1)  # just an example
        #     form = UserQueueForm(instance=game)
        #     return render_to_response('my_template.html', {'form': form})

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

class CalendarList(View):
    # login_url = '/login/'

    def get(self, request):
        calendar = ObservationList.objects.filter(date__lte=datetime.today())
        forward = ObservationList.objects.filter(date__gte=datetime.today()).order_by('date')

        return render(request, 'calendar-list.html', {'calendar': calendar, 'forward': forward})


class CalendarAdd(View):
    # login_url = '/login/'
    # redirect_field_name = '/login/'

    def get(self, request):
        form = Calendar()
        return render(request, 'calendar-add.html', {'form': form})

    def post(self, request):
        form = Calendar(request.POST)
        if form.is_valid():
            new_observation = form.save(commit=False)
            new_observation.scout = request.user
            new_observation.save()
            return redirect('/calendar/')
        else:
            return render(request, 'calendar-add.html', {'form': form})


class CalendarDeleteView(View):
    # login_url = '/login/'
    # redirect_field_name = '/login/'

    def get(self, request, id):
        calendar = ObservationList.objects.get(pk=id)
        return render(request, '', {'calendar': calendar})

    def post(self, request):
        calendar = ObservationList.objects.get(pk=id)
        calendar.delete()
        return redirect('/calendar/')

        # def post(self, request, id):
        #     room = Room.objects.get(id=id)
        #     room.delete()
        #     return redirect('/')

class AddCommentFormView(View):

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


class CommentDeleteView(View):
    def get(self, request, com_id, player_id):
        player = Player.objects.get(pk=player_id)
        comm = Comments.objects.get(pk=com_id)
        return render(request, 'delete-comment.html', {'player': player, 'comm': comm})
    def post(self, request, com_id, player_id):
        player = Player.objects.get(pk=player_id)
        comm = Comments.objects.get(pk=com_id)
        comm.delete()
        return redirect('/player/{}'.format(player.id))


