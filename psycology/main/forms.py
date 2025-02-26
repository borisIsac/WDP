from django import forms
from django.db import models

class ContactRequestForm(forms.Form):
    
    class Subjects(models.TextChoices):
        SELECT = 'Select an option', 'Select an option'
        BOOKS  = 'Books', 'Books'
        COURSES = 'Courses', 'Courses'
        MENTORSHIP = 'Mentorship', 'Mentorship'
        IMMERSIONS = 'Immersions', 'Immersions'

    full_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Insert your full name'})
        )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Insert your email'})
    )
    subject = forms.ChoiceField(
        choices = Subjects.choices,
        required=True,
        initial= Subjects.SELECT,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 40, 'placeholder': 'Write your message here'})
    )