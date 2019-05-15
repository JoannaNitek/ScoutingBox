from django.contrib import admin

# Register your models here.
from Users.models import UserData

admin.site.register(UserData)