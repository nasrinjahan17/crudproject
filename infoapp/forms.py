from django import forms
from django import forms
from .models import Student

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name' ,'email','class_no','password']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'class_no': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(render_value=True, attrs={'class':'form-control'}),
        }
        
# forms.PasswordInput(render_value=True) means by deafult it stay False. But when we make it True we password instant in edit form.