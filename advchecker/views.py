from django.shortcuts import render
from campagnes.models import Enseigne, Magasin


def index(request):
    campagnes_enseigne_list = Enseigne.objects.all()
    campagnes_magasin_list = {}
    for e in campagnes_enseigne_list:
        e_magasins_list = Magasin.objects.filter(enseigne=e)
        campagnes_magasin_list[e] = e_magasins_list
        print campagnes_magasin_list

    context = {'campagnes_enseigne_list': campagnes_enseigne_list,
               'campagnes_magasin_list': campagnes_magasin_list}
    return render(request, 'advchecker/index.html', context)


## Class based view
