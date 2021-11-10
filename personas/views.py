from personas.models import Domicilio
from personas.forms import DomicilioForm
from personas.forms import PersonaForm
from django.db import models
from personas.models import Personas
from django.shortcuts import get_object_or_404, redirect, render
from django.forms import modelform_factory

# Create your views here.
def detallePersona(request, id):
    #persona = Personas.objects.get(pk=id) #Si no encuentra el registro devuve un error
    persona = get_object_or_404(Personas, pk=id) #Si no encuentra envia el mensaje de error 404 y queda mas entendible
    return render(request, 'personas/detalle.html', {'persona':persona}) #Recupera el objeto y lo muestra

#PersonaForm = modelform_factory(Personas, exclude=[])
#ponemos en comentario la linea anterior y llamamos a la clase PersonaForm de forms.py
def nuevaPersona(request):
    '''Creamos una clase de DJANGO para crear un nuevo objeto en el cual va a tener el 
    #objeto de formulario relacionado a la clase de persona.'''

    if request.method == 'POST': #Como Post no guarda, necesitamos guardarlo a mano
        formaPersona = PersonaForm(request.POST) #pasamos los parametros
        if formaPersona.is_valid(): #si son validos los guardamos
            formaPersona.save()
            return redirect('index')

    else: #Si todavia no enviamos el POST, devolvemos el formulario para la carga de datos
        formaPersona = PersonaForm()
    
    return render(request, 'personas/nuevo.html', {'formaPersona':formaPersona})

def editarPersona(request,id):
    persona = get_object_or_404(Personas, pk=id)
    if request.method == 'POST': #Como Post no guarda, necesitamos guardarlo a mano
        formaPersona = PersonaForm(request.POST, instance=persona) #pasamos los parametros
        if formaPersona.is_valid(): #si son validos los guardamos
            formaPersona.save()
            return redirect('index')

    else: #Si todavia no enviamos el POST, devolvemos el formulario para la carga de datos
        formaPersona = PersonaForm(instance = persona)#DEBEMOS INDICAR LA INSTANCIA
    
    return render(request, 'personas/editar.html', {'formaPersona':formaPersona})

def eliminarPersona(request,id):
    persona = get_object_or_404(Personas, pk=id)
    if persona:
        persona.delete()
    return redirect('index')




''''-----------------------DOMICILIO------------------------------------'''
def detalleDomicilio(request):
    domicilio = Domicilio.objects.order_by('id')
    #domicilio = get_object_or_404(Domicilio) 
    return render(request, 'domicilio/detalle.html', {'domicilio':domicilio}) 

def nuevoDomicilio(request):

    if request.method == 'POST': 
        formaDomicilio = DomicilioForm(request.POST)
        if formaDomicilio.is_valid(): 
            formaDomicilio.save()
            return redirect('admin_dom')

    else: 
        formaDomicilio = DomicilioForm()
    
    return render(request, 'domicilio/nuevo.html', {'formaDomicilio':formaDomicilio})

def editarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if request.method == 'POST': #Como Post no guarda, necesitamos guardarlo a mano
        formaDomicilio = DomicilioForm(request.POST, instance=domicilio) #pasamos los parametros
        if formaDomicilio.is_valid(): #si son validos los guardamos
            formaDomicilio.save()
            return redirect('admin_dom')

    else: #Si todavia no enviamos el POST, devolvemos el formulario para la carga de datos
        formaDomicilio = DomicilioForm(instance = domicilio)#DEBEMOS INDICAR LA INSTANCIA
    
    return render(request, 'domicilio/editar.html', {'formaDomicilio':formaDomicilio})

def eliminarDomicilio(request,id):
    domicilio = get_object_or_404(Domicilio, pk=id)
    if domicilio:
        domicilio.delete()
    return redirect('admin_dom')

   
