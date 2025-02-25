from django import forms
from django.db import models

class ContactRequestForm(forms.ModelForm):
    
    class Subjects(models.TextChoices):
        SELECT = 'Select an option', 'Select an option'
        BOOKS  = 'Books', 'Books'
        COURSES = 'Courses', 'Courses'
        MENTORSHIP = 'Mentorship', 'Mentorship'
        IMMERSIONS = 'Immersions', 'Immersions'

    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.ChoiceField(
        choices = Subjects.choices,
        required=True,
        initial= Subjects.SELECT
    )
    message = forms.CharField(widget=forms.Textarea)