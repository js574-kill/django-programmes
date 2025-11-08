import json
from django.shortcuts import render
from django.conf import settings

def liste_identites(request):

    with open('fake/static/fake/data.json', encoding='utf-8') as f:
        identites = json.load(f)

    return render(request, 'fake/identites.html', {'identites': identites})
def accueil(request):
    return render(request, 'fake/accueil.html')

def detail_identite(request, id):
    with open('fake/static/fake/data.json', encoding='utf-8') as f:
        identites = json.load(f)

    personne = next((p for p in identites if p["id"] == id), None)

    if not personne:
        return render(request, '404.html', status=404)

    return render(request, 'fake/detail.html', {'personne': personne})