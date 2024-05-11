from django import forms
from django.contrib.auth.forms import UserCreationForm
from skin_cancer_app.models import Account
from django.contrib.auth import authenticate


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        max_length=255, help_text="Required. enter a valid email")

    class Meta:
        model = Account
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        try:
            obj = Account.objects.get(email=email)
        except Exception as e:
            return email
        raise forms.ValidationError(
            "The Email already in use. Try different one")

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            obj = Account.objects.get(username=username)
        except Exception as e:
            return username
        raise forms.ValidationError(
            "The Username already in use. Try different one")


class AccountAuthenticationForm(forms.ModelForm):

    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = Account
        fields = ("email", "password")

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        try:
            obj = Account.objects.get(email=email)
        except Exception as e:
            raise forms.ValidationError(
                "Invalid Login")
