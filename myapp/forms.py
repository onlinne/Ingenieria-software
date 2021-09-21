from django import forms
from myapp.models import User
from myapp.models import Auto

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class NewAutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = '__all__'
