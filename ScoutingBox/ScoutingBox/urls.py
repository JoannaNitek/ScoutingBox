"""ScoutingBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import patterns as patterns
from django.contrib import admin
from django.contrib.auth import login
from django.contrib.auth.views import redirect_to_login, LoginView
from django.urls import path, re_path
from Box.views import LandingPageView, PlayerListView, AddPlayerView, \
    PlayerView, ObservationFormView, CalendarAdd, CalendarList, PlayerEditView, CalendarDeleteView, ObservationFormPlayerView
from Users import views
from Users.views import LogIn, LogOut, Register
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('ScoutingBox/', LandingPageView.as_view()),
    path('players/', PlayerListView.as_view()),
    re_path('add_player/', AddPlayerView.as_view()),
    re_path(r'^player/(?P<player_id>(\d)+)', PlayerView.as_view()),
    path('form/', ObservationFormView.as_view()),
    re_path(r'^form/(?P<player_id>(\d)+)', ObservationFormPlayerView.as_view()),
    path('login/', LogIn.as_view()),
    path('register/', Register.as_view()),
    path('logout/', LogOut.as_view()),
    path('calendar/', CalendarList.as_view()),
    path('calendar_add/', CalendarAdd.as_view()),
    re_path(r'^edit_player/(?P<player_id>(\d)+)', PlayerEditView.as_view()),
    re_path(r'^delete_calendar/(?P<id>(\d)+)', CalendarDeleteView.as_view()),


              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
