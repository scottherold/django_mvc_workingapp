"""
This file is specific to generating Django user forms for the AppTwo
application.
"""
from django.forms import ModelForm
from AppTwo.models import User


class UserForm(ModelForm):
    """
    This class creates a Django ModelForm for the User model.
    """
    class Meta:
        """
        Attributes:
            model (User): Sets the UserForm model to tie to the User model.
            fields (list): Provides a list of fields to be mapped from the
            provided form data to the User model.
        """
        model = User
        fields = ['first_name', 'last_name', 'email']