from django.shortcuts import render
import wikipediaapi

def poets_list(request):
    wiki = wikipediaapi.Wikipedia('uz')
    page = wiki.page("Oʻzbekiston_poetlari")
    poets = page.links

    return render(request, 'poets_list.html', {'poets': poets})
