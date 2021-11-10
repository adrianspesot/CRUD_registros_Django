from typing import Text
from personas.models import Domicilio
from django.forms import ModelForm, widgets, EmailInput, TextInput 
from personas.models import Personas

class PersonaForm(ModelForm):
    class Meta:
        #Personalizamos el comportamiento de los atributos del formulario
        model = Personas #Recibe una referencia del objeto persona
        fields = '__all__' # indicamos que utilizamos todos los atributos de tipo persona
        widgets = {
            'email': EmailInput(attrs={'type':'email'})
        }

class DomicilioForm(ModelForm):
    class Meta:
        model = Domicilio 
        fields = '__all__' 
        widgets = {
            'no_calle': TextInput(attrs={'type':'number'})
        }
