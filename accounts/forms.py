from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = UserCreationForm.Meta.fields + ('username', 'email', 'age',)

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('username', 'email', 'age',) # new
		
		#fields = UserChangeForm.Meta.fields we’re using Meta.fields, which just displays
		#the default settings of username/age/password