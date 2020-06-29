from django import forms
from . models import MyModel,DecryptModel

class FileForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields=('file','password')

class DecryptForm(forms.ModelForm):
    class Meta:
        model=DecryptModel
        fields=('encryptedFile','password')