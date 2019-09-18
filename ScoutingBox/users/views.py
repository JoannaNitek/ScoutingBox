from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/accounts/login/')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })

# class SingUpView(View):
#
#     def get(self, request):
#         form = SignUpForm()
#         return render(request, 'signup.html', {'form': form})
#
#     def post(self, request):
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             new_user = form.save()
#             return redirect('/accounts/login/')
#         else:
#             return render(request, 'signup.html', {'form': form})

# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect
# from .forms import SignUpForm
#
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('email')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(email=username, password=raw_password)
#             login(request, user)
#             return redirect('accounts/login/')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})