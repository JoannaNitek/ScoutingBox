from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

POSITION = (
    (1, 'Bramkarz'),
    (2, 'Prawy obrońca'),
    (3, 'Lewy obrońca'),
    (4, 'Półlewy obrońca'),
    (5, 'Półprawy obrońca'),
    (6, 'Lewe skrzydło'),
    (7, 'Prawe skrzydło'),
    (8, 'Środkowy poocnik (8)'),
    (9, 'Defensywny pomocnik (6)'),
    (10, 'Rozgrywający (10)'),
    (11, 'Napastnik')
)

STATUS = (
    (1, 'Odrzucony'),
    (2, 'Do obserwacji'),
    (3, 'Wzmocnienie kadry'),
    (4, 'TOP')
)

POINTS = (
    (1, '1'),
    (1.5, '1,5'),
    (2, '2'),
    (2.5, '2,5'),
    (3, '3'),
    (3.5, '3,5'),
    (4, '4')
)

OBSERV = (
    (1, 'Na żywo'),
    (2, 'Wideo')
)

QUESTION = (
    (1, 'Gra w ofensywie'),
    (2, 'Gra w defensywie'),
    (3, 'Gra bez piłki'),
    (4, 'Cechy wolicjonalne'),
    (5, 'Inne'),
    (6, 'Wnioski'),
     ('1a', 'Technika użytkowa'),
     ('2a', 'Gra słabszą nogą'),
     ('3a', 'Siła'),
     ('4a', 'Koordynacja'),
     ('5a', 'Przyspieszenie'),
     ('6a', 'Agresja'),
     ('7a', 'Odpowiedzialność w grze'),
     ('8a', 'Skłonność do przecinania linii przeciwnika(wejściem/podaniem)'),
     ('9a', 'Pracowitość'),
     ('10a', 'Odbiór piłki'),
     ('11a', 'Gra w powietrzu'))


class ObservationList(models.Model):
    date = models.DateTimeField()
    match = models.CharField(max_length=200)
    # jak stworzyć regex
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200, null=True, blank=True)
    scout = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)


class Player(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField()
    mail = models.EmailField(null=True, blank=True)
    phone = models.IntegerField(null=True, blank=True)
    club = models.CharField(max_length=200)
    position = models.IntegerField(choices=POSITION)
    status = models.IntegerField(choices=STATUS)
    agent = models.TextField(verbose_name='Kontakt z agentem', null=True, blank=True)
    other1 = models.TextField(verbose_name='Uwagi', null=True, blank=True)
    other2 = models.TextField(verbose_name='Uwagi', null=True, blank=True)
    other3 = models.TextField(verbose_name='Uwagi', null=True, blank=True)


class ObservationForm(models.Model):
    scout = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)
# nie chcę usuwać danych stąd kiedy usuniemy scouta
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    observation = models.IntegerField(choices=OBSERV)
    first_desc = models.TextField(verbose_name='Gra w ofensywie')
    second_desc = models.TextField(verbose_name='Gra w defensywie')
    third_desc = models.TextField(verbose_name='Gra bez piłki')
    fourth_desc = models.TextField(verbose_name='Cechy wolicjonalne')
    fifth_desc = models.TextField(verbose_name='Inne')
    sixth_desc = models.TextField(verbose_name='Wnioski')
    one = models.FloatField(choices=POINTS, verbose_name='Technika użytkowa')
    two = models.FloatField(choices=POINTS, verbose_name='Gra słabszą nogą')
    three = models.FloatField(choices=POINTS, verbose_name='Siła')
    four = models.FloatField(choices=POINTS, verbose_name='Koordynacja')
    five = models.FloatField(choices=POINTS, verbose_name='Przyspieszenie')
    six = models.FloatField(choices=POINTS, verbose_name='Agresja')
    seven = models.FloatField(choices=POINTS, verbose_name='Odpowiedzialność w grze')
    eight = models.FloatField(choices=POINTS, verbose_name='Skłonność do przecinania linii przeciwnika(wejściem/podaniem)')
    nine = models.FloatField(choices=POINTS, verbose_name='Pracowitość')
    ten = models.FloatField(choices=POINTS, verbose_name='Odbiór piłki')
    eleven = models.FloatField(choices=POINTS, verbose_name='Gra w powietrzu')
