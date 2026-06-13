from django.forms import ModelForm
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        # Indicar el modelo que va a usar
        model = Task
        # Indicar los campos que va a usar de ese modelo
        fields = ['title', 'description', 'important']