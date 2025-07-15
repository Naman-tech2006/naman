from django import forms
from .models import ContactEntry
from django.contrib.auth.hashers import make_password

class ContactForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = ContactEntry
        fields = ['name', 'email', 'phone', 'password']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.password = make_password(self.cleaned_data['password'])  # hash password
        if commit:
            instance.save()
        return instance
    
class ContactEntryForm(forms.ModelForm):
    class Meta:
        model = ContactEntry
        fields = ['name', 'email','phone']