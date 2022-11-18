from django.shortcuts import render,redirect
from .models import Pessoa


# Create your views here.

def listar_pessoas(request):
    pessoa = Pessoa.objects.filter(Ativo=True)
    return render(request,'Pessoa.html', {'pessoa':pessoa})

def detalhe_pessoas(request, id):
    pessoa = Pessoa.objects.get(Ativo=True, id=id)
    return render(request,'detalhe_pessoa.html', {'pessoa':pessoa})

def cadastro_pessoa(request):
    pessoa_id = request.GET.get('id')
    if pessoa_id:
        pessoa = Pessoa.objects.get(id=pessoa_id)
        return render(request, 'registro_pessoa.html',{'pessoa':pessoa})
    return render(request, 'registro_pessoa.html')

def alterar_pessoa(request):
    Nome = request.POST.get('name')
    Telefone = request.POST.get('phone')
    Email = request.POST.get('mail')
    Foto = request.FILES.get('file')
    pessoa_id = request.POST.get('pessoa_id')
    if pessoa_id:
        pessoa = Pessoa.objects.get(id=pessoa_id)
        pessoa.Nome = Nome
        pessoa.Telefone = Telefone
        pessoa.Email = Email
        if Foto:
            pessoa.Foto = Foto
        pessoa.save()
    else:
        pessoa = Pessoa.objects.create(Nome=Nome, Telefone=Telefone, Email=Email, Foto=Foto)
    url='/pessoa/registro/{}'.format(pessoa.id)

    return redirect('http://localhost:8000/Pessoa/all/')

def deletar_pessoa(request,id):
    pessoa=Pessoa.objects.get(id=id)
    pessoa.delete()
    return redirect('http://localhost:8000/Pessoa/all/')

