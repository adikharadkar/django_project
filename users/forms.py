from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Created a user registration form class which inherits from UserCreationForm
class UserRegistrationForm(UserCreationForm):

    # Created a field i.e. email
    email = forms.EmailField()

    class Meta:

        # Specified that the UserRegistrationForm will interact with User model in the database
        model = User

        # Different fields to be contained by UserRegistrationForm (in the same order)
        fields = ['username', 'email', 'password1', 'password2']