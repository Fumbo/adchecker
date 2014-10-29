from django.views.generic import TemplateView

from models import Campagne, Enseigne, Magasin, Rayon


class CampagnesAll(TemplateView):
    template_name = "campagnes/index.html"

    def get_context_data(self, **kwargs):
        context = super(CampagnesAll, self).get_context_data(**kwargs)
        campagne_list = Campagne.objects.all()
        enseigne_list = Enseigne.objects.all()
        magasin_list = {}
        for e in enseigne_list:
            e_magasins_list = Magasin.objects.filter(enseigne=e)
            magasin_list[e] = e_magasins_list

        context['campagne_list'] = campagne_list
        context['enseigne_list'] = enseigne_list
        context['magasin_list'] = magasin_list
        return context


class CampagnesDetail(TemplateView):
    template_name = "campagnes/campagne_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CampagnesDetail, self).get_context_data(**kwargs)
        campagne_list = Campagne.objects.all()

        context['current_id'] = int(self.kwargs['campagne_id'])
        context['campagne_list'] = campagne_list
        return context
