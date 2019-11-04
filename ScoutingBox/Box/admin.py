from django.contrib import admin

# Register your models here.
from Box.models import Player, ObservationList, Comments, ObservationForm


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'year_of_birth', 'club', 'position', 'status', 'mail', 'phone', 'agent']


class ObservationListAdmin(admin.ModelAdmin):
    list_display = ['date', 'match', 'city', 'country', 'scout']


class CommentsAdmin(admin.ModelAdmin):
    list_display = ['comment', 'player', 'date']


class ObservationFormAdmin(admin.ModelAdmin):
    list_display = ['scout', 'player', 'observation', 'first_desc',
                    'second_desc', 'third_desc', 'fourth_desc', 'fifth_desc', 'sixth_desc',
                    'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']


admin.site.register(Player, PlayerAdmin),
admin.site.register(ObservationList, ObservationListAdmin),
admin.site.register(Comments, CommentsAdmin),
admin.site.register(ObservationForm, ObservationFormAdmin)