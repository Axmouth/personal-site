from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True,
                                  max_length=100,
                                  widget=forms.EmailInput(attrs={'class': 'form-control'}))
    subject = forms.CharField(required=True,
                              max_length=100,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    message = forms.CharField(required=True,
                              max_length=5000,
                              widget=forms.Textarea(attrs={'class': 'form-control'}))
