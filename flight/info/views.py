from django.shortcuts import render
from .functions import scrap_data


# Create your views here.
def teste(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        info = scrap_data(nome)
        if info:
            context = {"info": info}
        else:
            context = {
                "error": f"Não foi possível encontrar informações sobre a base: {nome}"
            }
        return render(request, "index.html", context)

    return render(request, "index.html")
