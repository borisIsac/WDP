import datetime
from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=256, required=True)    


class RegisterFormUser(forms.Form):
    GENDER_LIST = [
        ("SELECT", "Select"),
        ("MALE", "Male"),
        ("FAMELE", "Female")
    ]
        
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=256, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=256, required=True)
    full_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=20, required=False)
    username=forms.CharField(max_length=100, required=False)

    birthday = forms.DateField(
        widget=forms.SelectDateWidget(
            empty_label=("Choose Year", "Choose Month", "Choose Day"),
            years=range(1950, datetime.date.today().year + 1)
        )
    )
    
    gender = forms.ChoiceField(
        choices = GENDER_LIST,
        required=False
        )
    country = forms.CharField(max_length=100, required=False)
        

class RegisterFormCompanie(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), max_length=256, required=True)
    confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=256, required=True)
    companie_name = forms.CharField(max_length=100, required=True)
    billing_address = forms.CharField(max_length=100, required=True)
    shipping_address = forms.CharField(max_length=20, required=False)
    payment_method = forms.CharField(max_length=100, required=False)
    

    
class PasswordChangeForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput(), max_length=256, required=True)
    new_password = forms.CharField(widget=forms.PasswordInput(), max_length=256, required=True)
    new_password_confirm = forms.CharField(widget=forms.PasswordInput(), max_length=256, required=True)