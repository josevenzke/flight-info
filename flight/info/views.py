from django.shortcuts import render
from .functions import scrap_data


# Create your views here.
def teste(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        valores = scrap_data(nome)
        context={'valores':valores}
        return render(request,'index.html',context)

    return render(request,'index.html')
