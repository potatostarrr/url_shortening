from .validators import urlValidator
from  django import forms
class SubmitURLForm(forms.Form):
    url = forms.CharField(validators=[urlValidator], label='Submit')


