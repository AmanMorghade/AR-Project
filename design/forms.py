from django import forms
from .models import UserFurniture

class UserFurnitureForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-2 border rounded text-black',
            'placeholder': 'Enter furniture name'
        })
    )
    
    model_file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={
            'class': 'w-full p-2 border rounded text-black',
            'accept': '.glb'
        })
    )

    class Meta:
        model = UserFurniture
        fields = ['name', 'model_file']
