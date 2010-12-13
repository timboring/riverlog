from django.forms import ModelForm
from riverlog import models

class AddRunForm(ModelForm):
	class Meta:
		model = models.Run
