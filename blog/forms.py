from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength': '100'}
    ))
    email_address = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'maxlength': '100'}
    ))
    subject = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'maxlength': '100'}
    ))
    message = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'maxlength': '1000', 'rows': 8}
    ))
