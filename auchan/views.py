from django.http import HttpResponse
from django.template import RequestContext, loader

from auchan.models import Drive


# Create your views here.
def index(request):
    auchan_drives_list = Drive.objects.all()
    template = loader.get_template('auchan/index.html')
    context = RequestContext(request, {
        'auchan_drives_list': auchan_drives_list,
    })
    return HttpResponse(template.render(context))


def detail(request, drive_id):
    return HttpResponse("Hello, world. You're looking at the %s drive" % drive_id)
