from django import forms

from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

# from .model import UserProfile

class RegistrationForm(UserCreationForm):

	rol = (
		('AD', 'Admin'),
		('ST', 'Student'),
		('TE', 'Teacher')
		)
	role = forms.CharField(widget=forms.Select(choices=rol))
	email = forms.EmailField(required=True)

	class Meta:
		model = User 
		fields=('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role')

 	# def __init__(self, *args, **kwargs):
 	# 	super(RegistrationForm, self).__init__(*args, **kwargs)
 	# 	self.fields['role'].choices = [('AD','TE') for i in RegistrationForm.objects.filter(status='standard')]
	
	def save(self, commit=True):
		user = super(RegistrationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.email = self.cleaned_data['email']
		user.last_name = self.cleaned_data['last_name']

		if commit:
			user.save()
		return user
 

class EditProfileForm(UserChangeForm):

	class Meta:
		model = User
		fields = ('email', 'first_name', 'last_name', 'password')