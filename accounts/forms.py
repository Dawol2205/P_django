<<<<<<< HEAD
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = get_user_model()

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['profile_image']
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
=======
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = get_user_model()

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['profile_image']
        widgets = {
            'profile_image': forms.FileInput(attrs={'class': 'form-control'}),
>>>>>>> e86b7b9f37d611aad436361104d1f4cb0dea76e7
        }