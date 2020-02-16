from django.shortcuts import render, HttpResponse
from .models import Processo
# Create your views here.

def paginaInicial(request):
  processos = Processo.objects.all()
  return render(request,'processos/index.html', {"listaDeProcessos":processos})

def testeCss(request):  
  return render(request,'processos/base.html')

def listaProcessos(request):
  return HttpResponse("Listagem de Processos")
  
