from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import SaveFileContent
from processo. models import Processo
import pandas as pd
# Create your views here.
def homePage(request):
  if request.method == 'POST':
    
      form = SaveFileContent(request.POST)
                 
      processos = pd.read_csv(request.FILES['file'],delimiter =';').values      
      for row in processos:
        # print(row[1])          
        processo = Processo()
        processo.comarca = row[0]
        processo.pasta = row[1]
        processo.uf = row[2]
        processo.save()
      
      return HttpResponseRedirect('/processos/')

  else:
      form = SaveFileContent()
  return render(request,'cadastroprocessos/index.html',{'form':form})