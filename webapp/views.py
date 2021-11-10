from personas.models import Personas
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def benvenido(request):
   # return HttpResponse('Hola Mundo desde Django') #Regresa una cadena 
   no_personas = Personas.objects.count()
   #personas = Personas.objects.all() # RECUPERAMOS TODOS LOS OBJETOS
   personas = Personas.objects.order_by('id','nombre')
   return render(request, 'bienvenido.html',{'no_personas': no_personas, 'personas': personas}) #Esto se conoce como Templates


