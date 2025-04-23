from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label="Prenume")
    last_name = forms.CharField(max_length=30, required=False, label="Nume")
    email = forms.EmailField(required=True, label="Email")
    is_admin = forms.BooleanField(required=False, label="Administrator")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name', 'email']
