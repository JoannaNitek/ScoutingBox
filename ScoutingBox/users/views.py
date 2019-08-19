from django.shortcuts import render, redirect
from django.views import View

# Create your views here.

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