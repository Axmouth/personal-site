from django import forms


class ContactForm(forms.Form):
    from_email = forms.EmailField(label='Your email',
                                  required=True,
                                  max_length=100,
                                  widget=forms.EmailInput(attrs={
                                      'class': 'form-control',
                                      'aria-required': 'true',
                                  }))
    subject = forms.CharField(label='Message Subject',
                              required=True,
                              max_length=100,
                              widget=forms.TextInput(attrs={
                                      'class': 'form-control',
                                      'aria-required': 'true',
                                  }))
    message = forms.CharField(label='Your Message',
                              required=True,
                              max_length=5000,
                              widget=forms.Textarea(attrs={
                                      'class': 'form-control',
                                      'aria-required': 'true',
                                  }))
