# forms.py
from django import forms
from .models import Church

class ChurchForm(forms.ModelForm):
    class Meta:
        model = Church
        fields = ['name', 'denomination', 'address', 'phone', 'email']


# forms.py in your existing app
from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
