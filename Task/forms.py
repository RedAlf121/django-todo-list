from .models import Task
from django.forms import ModelForm,DateInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name','description','date']
        widgets = {
            'date': DateInput(attrs={'type':'date'})
        }