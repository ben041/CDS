# disease_detector/forms.py
from django import forms

class SymptomForm(forms.Form):
    symptoms = forms.CharField(
        label="Enter the symptoms you are experiencing, separated by commas",
        widget=forms.Textarea(attrs={'placeholder': 'e.g., fever, cough', 'class': 'form-control', 'rows': 4}),
        max_length=255,
        required=True,
    )
