from django.http import HttpResponse
from django.shortcuts import render

from campagnes.models import Magasin


# Create your views here.
def index(request):
    campagnes_magasins_list = Magasin.objects.all()
    context = {'campagnes_magasins_list': campagnes_magasins_list}
    return render(request, 'campagnes/index.html', context)


def detail(request, magasin_id):
    return HttpResponse("Hello, world. %s drive" % magasin_id)
