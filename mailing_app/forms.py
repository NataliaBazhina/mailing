from django import forms
from mailing_app.models import Mailing


class MailingForm(forms.ModelForm):
    class Meta:
        model = Mailing
        fields = ['first_mailing', 'frequency', 'clients', 'mail']
        widgets = {
            'first_mailing': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'time_next_mailing':  forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'frequency': forms.Select(attrs={'class': 'form-control'}),
            'clients': forms.CheckboxSelectMultiple(attrs={'class': 'form-control'}),
            'mail': forms.Select(attrs={'class': 'form-control'}),
        }
