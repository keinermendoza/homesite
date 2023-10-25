from django import forms

class ContactEmail(forms.Form):
    email = forms.EmailField()
    body = forms.TextInput()
    