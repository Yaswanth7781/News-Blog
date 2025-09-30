from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CustomUserCreationForm(UserCreationForm):
    # Add an email field and make it required.
    email = forms.EmailField(
        required=True, 
        help_text='Required. Please enter a valid email address.'
    )

    class Meta(UserCreationForm.Meta):
        model = User
        # Add 'email' to the list of fields to display on the form.
        fields = UserCreationForm.Meta.fields + ('email',)