from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Accounts.models import Town
from django import forms


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')


class TownChange(forms.ModelForm):
    class Meta:
        model = Town
        fields = ('town', 'adres')


class NameChange(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class EmailChange(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
