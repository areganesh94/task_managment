from django.shortcuts import render

# Create your views here.


from account.forms import RegistrationForm, EditProfileForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


def home(request):
	return redirect('/account/profile')

def view_profile(request):
	args = {'user':request.user}
	return render(request, 'account/profile.html', args)

def register(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			print('^'*100)
			print(request.POST)
			
			form.save()
			return redirect('/account/profile')
	else:
		form = RegistrationForm()

	args = {'form':form}
	return render(request, 'account/reg_form.html', args)


@login_required
def view_profile(request):
	args = {'user':request.user}
	return render(request, 'account/profile.html', args)

def edit_profile(request):
	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('account/profile')

	else:
		form = EditProfileForm(instance=request.user)

		args={'form':form}
		return render(request, 'account/edit_profile.html', args)

def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/account/profile')
		else:
			return redirect('/account/change-password')

	else:
		form = PasswordChangeForm(user=request.user)

		args={'form':form}
		return render(request, 'account/change_password.html', args)