
from django import forms
from .models import Protein

class proteinForm(forms.ModelForm):
	
	class Meta():
		model = Protein
		fields = '__all__'