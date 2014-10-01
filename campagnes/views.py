from django.http import HttpResponse
from django.shortcuts import render

from campagnes.models import Drive


# Create your views here.
def index(request):
    campagnes_drives_list = Drive.objects.all()
    context = {'campagnes_drives_list': campagnes_drives_list}
    return render(request, 'campagnes/index.html', context)


def detail(request, drive_id):
    return HttpResponse("Hello, world. %s drive" % drive_id)
