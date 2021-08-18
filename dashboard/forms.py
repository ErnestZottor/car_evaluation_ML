from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from . models import CarEvaluation
class CarEvaluationForm(ModelForm):
    class Meta:
        model = CarEvaluation
        fields = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']