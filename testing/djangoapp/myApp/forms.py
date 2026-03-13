from django import forms
from .models import User, Contact

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','email','message']