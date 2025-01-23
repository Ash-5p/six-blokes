from django import forms
from allauth.account.forms import SignupForm
from django.contrib.auth.models import User  # Correct import for User model

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        
        # Add the 'name' field at the top
        self.fields['name'] = forms.CharField(
            required=True,
            label="Full Name",
            widget=forms.TextInput(attrs={'placeholder': 'Enter your full name'})
        )
        
        # Rearrange the order of fields to put 'name' first
        self.fields = {
            'name': self.fields['name'],
            **self.fields  # Retain all other fields in their original order
        }

    def save(self, request):
        # Save the user object
        user = super(CustomSignupForm, self).save(request)
        
        # Get the 'name' field from the cleaned data
        name = self.cleaned_data.get('name')

        # Set the first_name and last_name fields of the user
        if name:
            user.first_name = name.split(' ')[0]  # Use the first part of the name
            if len(name.split(' ')) > 1:
                user.last_name = ' '.join(name.split(' ')[1:])  # Optional: Set the last name
            else:
                user.last_name = ''  # Clear the last name if not provided
        
        # Save the updated user object
        user.save()
        
        return user
