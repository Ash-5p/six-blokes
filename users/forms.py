from django import forms
from allauth.account.forms import SignupForm

class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super(CustomSignupForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(required=True)
    def save(self, request):
        name = self.cleaned_data.pop('name')
        ...
        user = super(CustomSignupForm, self).save(request)