from django import forms

class StudentForm(forms.Form):
    name = forms.CharField(
        label='Nombre', 
        max_length=255,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    age = forms.IntegerField(
        label='Edad',
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='Correo electrónico',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
