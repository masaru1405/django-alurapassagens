from django.shortcuts import render
from .forms import PassagemForms, PessoaForms

def index(request):
   form = PassagemForms()
   pessoa_form = PessoaForms()
   context = {'form':form, 'pessoa_form':pessoa_form}
   return render(request, 'passagens/index.html', context)

def revisao_consulta(request):
   if request.method == 'POST':
      form = PassagemForms(request.POST)
      pessoa_form = PessoaForms(request.POST)
      context = {'form':form, 'pessoa_form':pessoa_form}
      if form.is_valid():
         return render(request, 'passagens/minha_consulta.html', context)
      print('Form inválido')
      return render(request, 'passagens/index.html', context)
