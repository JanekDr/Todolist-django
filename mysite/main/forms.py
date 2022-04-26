from django import forms

class CreateNewList(forms.Form):
    name = forms.CharField(max_length=300, label="Name")
    check = forms.BooleanField(required=False)
