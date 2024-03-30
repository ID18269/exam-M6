from django.shortcuts import render

from django.http import HttpResponse

links = f""

def Uzbek_poets(request):
    return render(request, "../uzbek_poets/../templates/Poetlar.html")
    #return HttpResponse('<h1>O\'zbek shoirlari</h1>'  + links)

def shoirlar(request):
    return render(request, "../uzbek_poets/../templates/Shoirlar.html")

def shoirlarning_rasmlari(request):
    return render(request, "../uzbek_poets/../templates/rasmlari.html", {"links": links})



