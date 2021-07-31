from django import forms

class phoneForm(forms.Form):

    phonenumber = forms.CharField()






class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

