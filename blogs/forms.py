from django import forms
from .models import BlogContent

class TestFormClass(forms.Form):
    name = forms.CharField(max_length=100)
    roll_no = forms.IntegerField()
    school_name = forms.CharField(max_length=100)

class ModelsDemoForm(forms.ModelForm):
    class Meta:
        model = BlogContent
        fields = '__all__'
        
