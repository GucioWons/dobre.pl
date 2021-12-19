from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
from Pages.forms import SignUpForm


def register_page(request):
    form = SignUpForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home-view")
    context={
        "form":form
    }
    return render(request, "register_view.html", context)

def login_page(request):
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
    logout(request)
    return redirect("home-view")

def home_page(request):
    return render(request, "home_view.html", context={})
