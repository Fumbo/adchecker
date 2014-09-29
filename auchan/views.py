from django.http import HttpResponse
from django.shortcuts import render

from auchan.models import Drive


# Create your views here.
def index(request):
    auchan_drives_list = Drive.objects.all()
    context = {'auchan_drives_list': auchan_drives_list}
    return render(request, 'auchan/index.html', context)


def detail(request, drive_id):
    return HttpResponse("Hello, world. %s drive" % drive_id)
