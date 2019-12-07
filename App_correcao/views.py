from django.shortcuts import render,redirect
from .models import Funcionario,Solicitacao,Veiculo
from .forms import SoliForm

def lista(request):

    sol = Solicitacao.objects.filter(solicitante__usuario=request.user)
    return render(request,'lista.html',{'sol':sol})

def cargo(request):
    fun = Funcionario.objects.get(usuario=request.user)
    sol = Solicitacao.objects.all()

    if fun.cargo.eh_chefe and fun.departamento.eh_transporte:
        return render(request,'lista_tranporte.html',{'sol':sol})
    else:
        return render(request,'erro.html')

def solicitar(request):

    if request.method =='POST':
        form = SoliForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, 'solicitar.html', {'form': form})
    else:
        form = SoliForm(request.POST)
        return render(request,'solicitar.html',{'form':form})