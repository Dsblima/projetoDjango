from django import forms

class SaveFileContent(forms.Form):
  file = forms.FileField(label='Escolher arquivo')