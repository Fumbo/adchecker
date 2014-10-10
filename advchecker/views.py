from django.views.generic import TemplateView
from campagnes.models import Enseigne, Magasin


## Class based view
class HomeView(TemplateView):
    template_name = "advchecker/index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        campagnes_enseigne_list = Enseigne.objects.all()
        campagnes_magasin_list = {}
        for e in campagnes_enseigne_list:
            e_magasins_list = Magasin.objects.filter(enseigne=e)
            campagnes_magasin_list[e] = e_magasins_list

        context['campagnes_enseigne_list'] = campagnes_enseigne_list
        context['campagnes_magasin_list'] = campagnes_magasin_list
        return context
