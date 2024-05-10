from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm,PasswordChangeForm

# Create your views here.
class loginView(View):
    def get(self, request, *args, **kwargs):
        form = AuthenticationForm
        return render(request,'accounts/login.html', {'form': form})
    def post(self, request, *args, **kwargs):
        if 'password' in request.POST:  # Check if login button is submitted
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')  # Redirect to dashboard or any other page
                else:
                    print('Please enter')
                    messages.error(request, 'Invalid username or password.')  # Display error message
        else:
            form = AuthenticationForm
        return render(request, 'accounts/login.html', {'form': form})

class logoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('home')

class registerView(View):
    def get(self, request, *args, **kwargs):
        form = UserCreationForm
        return render(request,'accounts/register.html', {'form': form})
    def post(self, request, *args, **kwargs):
        if 'password1' in request.POST:  # Check if login button is submitted
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()  # Save the new user
                return redirect('profile')  # Redirect to login page after successful registration
        else:
            form = UserCreationForm
        return render(request, 'accounts/register.html', {'form': form})


class passwordChangeView(View):
    def get(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user)  # Pre-populate with current user
        return render(request, 'accounts/password-change.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()  # Update user object with new password
            update_session_auth_hash(request, user)  # Update session auth hash
            return redirect('profile')  # Redirect to profile page after successful change
        else:
            return render(request, 'accounts/password-change.html', {'form': form})


