from django.db import models

# Createe your models here.

from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.contrib.auth.forms import UserCreationForm

class UserProfile(models.Model):
	
	user 		= models.OneToOneField(User)
	status 		= models.TextField(max_length=100)
	

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)