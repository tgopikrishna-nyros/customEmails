from django import forms

def is_anagram(x, y):
	return sorted(x) == sorted(y)
 
class AnagramForm(forms.Form):
	test_value = forms.CharField(
		lebel='Your name',
		max_length=100,
		widget=forms.TextInput(attrs={'class' : "input"}))
	def clean_test_value(self):
		data = self.cleaned_data.get('test_value')
		
		if not is_anagram(data, 'listen'):
			raise forms.ValidationError('This is not valid')
		
		return data
