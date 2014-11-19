from django.views.generic import TemplateView

from models import Campagne, PlanificationCampagne


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
    template_name = "campagnes/detail_v2.html"

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
        context['campagne_list'] = campagne_list
        context['nb_campagne'] = len(campagne_list)
        context['allowed_user'] = current_campagne.user
        context['tests'] = PlanificationCampagne.objects.filter(campagne_id=current_campagne.id)
        return context
