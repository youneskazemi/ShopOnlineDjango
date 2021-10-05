from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import User


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully!', 'success')
                return redirect("shop:home")
            else:
                messages.warning(request, 'invalid email or password!', 'warning')
                return HttpResponseRedirect(request.path_info)

    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.success(request, 'logged out successfully!', 'success')
    return redirect('accounts:login')


def user_register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(email=form.cleaned_data['email'], full_name=form.cleaned_data['full_name'],
                                            password=form.cleaned_data['password1'])
            user.save()
            messages.success(request, 'registered successfully!', 'success')
            return redirect("accounts:login")
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
