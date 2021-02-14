from django import forms

class ContactForm(forms.Form):
    contactName = forms.CharField(max_length=100)
    contactEmail = forms.EmailField()
    contactSubject=forms.CharField(max_length=100)
    contactMessage = forms.CharField(widget=forms.Textarea)