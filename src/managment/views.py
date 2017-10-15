from django.shortcuts import redirect

from django.contrib.auth.models import User

def login_redirect(request):
	if User.is_authenticated:
		return redirect('account/profile')
	else:
		return redirect('account/login')