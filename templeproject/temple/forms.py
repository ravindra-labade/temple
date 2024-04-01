from django import forms
from .models import Temple


class TempleForm(forms.ModelForm):
    class Meta:
        model = Temple
        fields = "__all__"

        widgets = {
            "temple_name": forms.TextInput(attrs={'class': 'form-control'}),
            "famous_for": forms.TextInput(attrs={'class': 'form-control'}),
            "temple_address": forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            "state": forms.TextInput(attrs={'class': 'form-control'}),
            "devotees_per_day": forms.NumberInput(attrs={'class': 'form-control'}),
            "donation_mode": forms.Select(attrs={'class': 'form-control'}),
        }
