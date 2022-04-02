from django import forms
from django.contrib.auth import get_user_model
from .models import User

# User = get_user_model()


class RegistrationForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(min_length=6, widget=forms.PasswordInput, required=True)
    password_confirm = forms.CharField(min_length=6, widget=forms.PasswordInput, required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот email уже занят')
        return email

    def clean(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.pop('password_confirm')
        if password1 != password2:
            raise forms.ValidationError('Пароли не совпадают')
        return self.cleaned_data

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(**data)
        user.set_activation_code()
        user.send_activation_mail(
        )