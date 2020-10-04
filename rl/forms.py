from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.forms import ModelForm
from .models import *


class AddStartup(forms.Form):
    """
    Add new startup details.
    """
    name = forms.CharField(
        label="Name",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "fname",
                "required": "yes",
                "placeholder": "Company Name",
            }
        ),
    )

    flon = forms.CharField(
        label="Longitude",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "lname",
                "required": "yes",
                "placeholder": "",
            }
        ),
    )

    flat = forms.CharField(
        label="Lattitude",
        max_length=30,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "location",
                "required": "yes",
                "placeholder": "",
            }
        ),
    )

    date = forms.ChoiceField(
        label="Founded in", choices=[(x, x) for x in range(1900, 2018)]
    )
    link = forms.CharField(
        label="url",
        max_length=30,
        widget=forms.TextInput(
            attrs={"class": "form-control", "name": "company", "placeholder": ""}
        ),
    )


class TimeForm(forms.Form):
    dat = forms.ChoiceField(
        label="Founded in", choices=[(x, x) for x in range(1900, 2018)]
    )


class JoinForm(forms.Form):
    """
    Signup for new users
    """
    mail = forms.CharField(
        label="E-Mail",
        max_length=75,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "name": "email",
                "required": "yes",
                "placeholder": "E-Mail Address",
            }
        ),
    )

    fname = forms.CharField(
        label="First Name",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "fname",
                "required": "yes",
                "placeholder": "First Name",
            }
        ),
    )

    sname = forms.CharField(
        label="Last Name",
        max_length=50,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "name": "lname",
                "required": "yes",
                "placeholder": "Last Name",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "id": "rpassword",
                "name": "password",
                "required": "yes",
                "placeholder": "Password (Minimum 6 characters)",
            }
        ),
    )

    cpswd = forms.CharField(
        label="Retype Password",
        max_length=100,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "onkeyup": "check()",
                "name": "password",
                "required": "yes",
                "placeholder": "Retype Password",
            }
        ),
    )


class JoinLog(forms.Form):
    pswd = forms.CharField(
        label="Password",
        max_length=30,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "name": "password",
                "required": "yes",
                "placeholder": "Password",
            }
        ),
    )
    mail = forms.CharField(
        label="E-Mail",
        max_length=75,
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "name": "email",
                "required": "yes",
                "placeholder": "E-Mail Address",
            }
        ),
    )
