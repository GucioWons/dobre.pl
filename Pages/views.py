from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

# Create your views here.
from Accounts.models import Cart, Town
from Pages.forms import SignUpForm, TownChange, NameChange, EmailChange


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        Cart.objects.create(user=user)
        Town.objects.create(user=user)
        return redirect("home-view")
    context = {
        "form": form
    }
    return render(request, "register_view.html", context)


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print("dupa")
                return redirect('/')
            else:
                print("dupa")
        else:
            print("dupa")
    form = AuthenticationForm()
    return render(request, "login_view.html", context={"form": form})


def logout_view(request):
    if not request.user.is_authenticated:
        return redirect('/landing')
    logout(request)
    return redirect("home-view")


def settings_page(request):
    if not request.user.is_authenticated:
        return redirect('/landing')
    form = TownChange(request.POST or None, instance=get_object_or_404(Town, user=request.user))
    form2 = NameChange(request.POST or None, instance=request.user)
    form3 = EmailChange(request.POST or None, instance=request.user)
    if 'change_town' in request.POST:
        if form.is_valid():
            form.save()
    elif 'change_name' in request.POST:
        if form2.is_valid():
            form2.save()
    elif 'change_email' in request.POST:
        if form3.is_valid():
            form3.save()
    return render(request, "settings_view.html", context={"form": form, "form2": form2, "form3": form3})


def home_page(request):
    if not request.user.is_authenticated:
        return redirect('/landing')
    return render(request, "home_view.html", context={})


def landing_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request, "landing_view.html", context={})
