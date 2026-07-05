from django import forms
from .models import UserProfile

# Section C - Question 1: Create/Edit via Django Forms using ModelForms.
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'age', 'is_public']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter your age'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

    # Section B - Question 2: Create ModelForm & Validation with clean_age() to enforce constraints.
    def clean_age(self):
        age = self.cleaned_data.get('age')
        if age is not None and age <= 13:
            raise forms.ValidationError("User must be over 13 years old.")
        return age
