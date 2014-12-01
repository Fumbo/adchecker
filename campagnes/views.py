from django.views.generic import TemplateView

from campagnes.models import Campagne, PlanificationCampagne, Rayon, Magasin, Enseigne


class CampagnesAll(TemplateView):
    template_name = "campagnes/index.html"

    def get_context_data(self, **kwargs):
        context = super(CampagnesAll, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            campagne_list = Campagne.objects.all()
            context['super'] = True
        else:
            campagne_list = Campagne.objects.filter(user_id=self.request.user.id)
        context['campagne_list'] = campagne_list
        context['nb_campagne'] = len(campagne_list)
        return context


class CampagnesDetail(TemplateView):
    template_name = "campagnes/campagne_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CampagnesDetail, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            campagne_list = Campagne.objects.all()
            context['super'] = True
        else:
            campagne_list = Campagne.objects.filter(user_id=self.request.user.id)
        current_campagne = Campagne.objects.get(id=context['campagne_id'])
        if current_campagne.user.id == self.request.user.id or self.request.user.is_superuser:
            context['current_campagne'] = current_campagne
            context['is_allowed'] = True
        context['campagne_list'] = campagne_list
        context['nb_campagne'] = len(campagne_list)
        context['tests'] = PlanificationCampagne.objects.filter(campagne_id=current_campagne.id)
        return context


class CampagnesNew(TemplateView):
    template_name = "campagnes/nouvelle_campagne.html"

    def get_context_data(self, **kwargs):
        context = super(CampagnesNew, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            campagne_list = Campagne.objects.all()
            context['super'] = True
        else:
            campagne_list = Campagne.objects.filter(user_id=self.request.user.id)
        context['campagne_list'] = campagne_list
        context['nb_campagne'] = len(campagne_list)
        context['rayons'] = self.get_complete_tree()
        return context

    def get_complete_tree(self):
        enseignes = Enseigne.objects.all()
        for enseigne in enseignes:
            yield 'in'
            yield enseigne
            magasins = Magasin.objects.filter(enseigne=enseigne.id)
            if len(magasins):
                for magasin in magasins:
                    yield 'in'
                    yield magasin
                    rayons = Rayon.objects.filter(parent=None, magasin=magasin.id)
                    if len(rayons):
                        yield 'in'
                        for x in self.get_rayon_tree(magasin_id=magasin.id):
                            yield x
                        yield 'out'
                yield 'out'
        yield 'out'

    def get_rayon_tree(self, rayons=None, magasin_id=None):
        """Recursively build a list of rayons. The resulting list is meant to be iterated over in a view"""
        if rayons is None:
            # get the root rayons
            rayons = Rayon.objects.filter(parent=None, magasin=magasin_id)
            rayons[0].active = True
        else:
            yield 'in'

        for rayon in rayons:
            yield rayon.nom
            sub_cats = Rayon.objects.select_related().filter(parent=rayon, magasin=magasin_id)
            if len(sub_cats):
                rayon.leaf = False
                for x in self.get_rayon_tree(sub_cats, magasin_id):
                    yield x
            else:
                rayon.leaf = True
        yield 'out'
