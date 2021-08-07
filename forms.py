from django import forms  
from student.models import Employee  
class studentForm(forms.ModelForm):  
    class Meta:  
        model = student  
        fields = "__all__"  