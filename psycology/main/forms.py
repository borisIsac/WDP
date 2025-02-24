from django import forms
from .models import ContactRequest

class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = [
            'full_name',
            'email',
            'subject',
            'message',
        ]