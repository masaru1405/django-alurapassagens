from django.shortcuts import render
from .forms import PassagemForms

def index(request):
   form = PassagemForms()
   context = {'form':form}
   return render(request, 'passagens/index.html', context)

def revisao_consulta(request):
   if request.method == 'POST':
      form = PassagemForms(request.POST)
      context = {'form':form}
      return render(request, 'passagens/minha_consulta.html', context)
