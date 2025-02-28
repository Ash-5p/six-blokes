from django import forms
from allauth.account.forms import SignupForm


class CustomSignupForm(SignupForm):
    '''
    Sign up form - Modifies the default allauth signup form
    to include name input.
    '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(
            required=True,
            label="Full Name",
            widget=forms.TextInput(attrs={
                'placeholder': 'Enter your full name'
            }),
        )

        self.fields = {
            'name': self.fields['name'],
            **self.fields
        }

    def save(self, request):

        user = super(CustomSignupForm, self).save(request)
        name = self.cleaned_data.get('name')

        if name:
            user.first_name = name.split(' ')[0]
            if len(name.split(' ')) > 1:
                user.last_name = ' '.join(name.split(' ')[1:])
            else:
                user.last_name = ''

        user.save()

        return user
