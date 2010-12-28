from django import forms
from riverlog import models

class AddRunForm(forms.ModelForm):
	class Meta:
		model = models.Run

class UploadFileForm(forms.Form):
	filename = forms.FileField()
