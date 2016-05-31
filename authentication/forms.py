from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.admin import User


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                               label="Username",
                               widget=forms.TextInput())
    password = forms.CharField(max_length=100,
                               label="Password",
                               widget=forms.PasswordInput())

    def validate(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is None:
            message = 'Username or password is incorrect'
            self.add_error('username', message)
            return False

        if not user.is_active:
            message = 'User is not activated'
            self.add_error('username', message)
            return False

        return True


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(max_length=100,
                                       label="Current password",
                                       widget=forms.PasswordInput())
    new_password = forms.CharField(max_length=100,
                                   label="New password",
                                   widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(max_length=100,
                                           label="Confirm password",
                                           widget=forms.PasswordInput())

    def validate(self, user):
        current = self.cleaned_data["current_password"]
        new = self.cleaned_data["new_password"]
        confirm = self.cleaned_data["confirm_new_password"]

        if not user.check_password(current):
            message = "Current password is wrong"
            self.add_error('current_password', message)
            return False

        if not new == confirm:
            message = "Passwords does not match"
            self.add_error('current_password', message)
            return False
        return True


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=100,
                               label="Username",
                               widget=forms.TextInput())
    email = forms.EmailField(max_length=100,
                             label="Email",
                             widget=forms.EmailInput())
    first_name = forms.CharField(max_length=50,
                                 label="First name",
                                 widget=forms.TextInput())
    last_name = forms.CharField(max_length=50,
                                label="Last name",
                                widget=forms.TextInput())
    new_password = forms.CharField(max_length=100,
                                   label="New password",
                                   widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(max_length=100,
                                           label="Confirm password",
                                           widget=forms.PasswordInput())

    def validate(self):
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']

        try:
            User.objects.get(username=username)
            message = 'Username already exists'
            self.add_error('username', message)
            return False
        except User.DoesNotExist:
            pass

        try:
            User.objects.get(email=email)
            message = 'Email is already registered'
            self.add_error('email', message)
            return False
        except User.DoesNotExist:
            pass

        if not(str(email).endswith('@stud.ntnu.no') or str(email).endswith('@ntnu.no') or str(email).endswith(
                '@ntnu.edu')):
            message = 'Email is not from NTNU'
            self.add_error('email', message)
            return False

        if not new_password == confirm_new_password:
            message = 'Passwords does not match'
            self.add_error('new_password', message)
            self.add_error('confirm_new_password', message)
            return False

        return True


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(max_length=100,
                             label='Email',
                             widget=forms.TextInput())

    def validate(self):
        email = self.cleaned_data['email']
        try:
            User.objects.get(email=email)
            return True
        except User.DoesNotExist:
            message = "Email is not registred"
            self.add_error("email", message)
            return False


class SetPasswordForm(forms.Form):
    new_password = forms.CharField(max_length=100,
                                   label="New password",
                                   widget=forms.PasswordInput())
    confirm_new_password = forms.CharField(max_length=100,
                                           label="Confirm password",
                                           widget=forms.PasswordInput())

    def validate(self):
        new_password = self.cleaned_data['new_password']
        confirm_new_password = self.cleaned_data['confirm_new_password']

        if not new_password == confirm_new_password:
            message = "Passwords does not match"
            self.add_error('new_password', message)
            self.add_error('confirm_new_password', message)
            return False
        return True
