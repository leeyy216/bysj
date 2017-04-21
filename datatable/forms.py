from django import forms

class enrollForm(forms.Form):
	from_sch = forms.CharField(max_length = 30)
	stu_num = forms.CharField(max_length = 30)
	stu_name = forms.CharField(max_length = 30)
	into_sch = forms.CharField(max_length = 30)
	
