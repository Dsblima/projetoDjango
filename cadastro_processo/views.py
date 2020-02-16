from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .forms import SaveFileContent
from processo. models import Processo
import pandas as pd
# Create your views here.
def homePage(request):
  if request.method == 'POST':
    #   print("request")
    #   print(request.FILES)
      # create a form instance and populate it with data from the request:
      form = SaveFileContent(request.POST)
      print("linhas do arquivo")
            
      processos = pd.read_csv(request.FILES['file'],delimiter =';').values      
      for row in processos:
        # print(row[1])          
        processo = Processo()
        processo.comarca = row[0]
        processo.pasta = row[1]
        processo.uf = row[2]
        processo.save()
      # check whether it's valid:
      # if form.is_valid():
          # process the data in form.cleaned_data as required
          # ...
          # redirect to a new URL:
      return HttpResponseRedirect('/processos/')

  # if a GET (or any other method) we'll create a blank form
  else:
      form = SaveFileContent()
  return render(request,'cadastroprocessos/index.html',{'form':form})