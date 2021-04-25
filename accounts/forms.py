from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms import DateInput
from phonenumber_field.formfields import PhoneNumberField

from accounts.models import Kandidat, User


class MyLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class MyForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
    phone = PhoneNumberField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'birth_date', 'password', 'password2',)
        widgets = {
            'birth_date': DateInput(attrs={'type': 'date'}),
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    @transaction.atomic
    def save(self):
        user = super().save()
        user.is_kandidat = True
        user.birth_date = self.cleaned_data["birth_date"]
        user.phone = self.cleaned_data["phone"]
        user.save()
        kandidat = Kandidat.objects.create(user=user)
        kandidat.save()
        return user
