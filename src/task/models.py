from django.db import models

from django.contrib.auth.models import User

from account.forms import RegistrationForm

# Create your models here.

# if User.is_authenticated:
	
	

class Task(models.Model):
	description = models.CharField(max_length=120)
	title		= models.TextField(max_length=100)
	user 		= models.ForeignKey(User)

	types = (
		('todo', 'To-Do list'),
		('do', 'Doing List'),
		('Don', 'Done List')
		)
	active_feed = models.CharField(max_length=100,choices=types, default='todo')
	work_satisfaction = (
		('approve','approved'),
		('disapprove', 'disapproved')
		)
	sanction = models.CharField(max_length=100,choices=work_satisfaction, default='approve')

	def __str__(self):
		return self.title









# Super Admin
# Logins:-(Email Considered)__Signup and login 
# 		Email
# Admin
# Student
# Teacher

# python -m smtpd -n -c DebuggingServer localhost:1025

# Login Page (News Feed)
# Super_Admin	--> Delete Task
# Admin		--> Create Task/approved/disapproved
# Teacher		--> Create Task/approved/disapproved
# Student		--> 
# <->	todo
# <-> 	doing
# <-> 	done

# 2 Apps For Task And Accout 
# 		