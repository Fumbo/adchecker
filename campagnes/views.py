from django import forms
from django.views.generic import TemplateView, FormView

from mptt import forms as mptt_forms
from campagnes.models import Campagne, PlanificationCampagne, Rayon, Enseigne


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


class CampagnesNewForm(forms.Form):
    nom = forms.CharField()
    enseignes = forms.MultipleChoiceField(choices=Enseigne.objects.all().values_list('id', 'nom'),
                                          widget=forms.CheckboxSelectMultiple)
    rayons = mptt_forms.TreeNodeMultipleChoiceField(queryset=Rayon.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple,
                                                    level_indicator=u'')
    date_debut = forms.DateField()
    date_fin = forms.DateField()


class CampagnesNew(FormView):
    template_name = "campagnes/nouvelle_campagne.html"
    form_class = CampagnesNewForm
    success_url = '/campagnes/'

    def form_valid(self, form):
        return super(CampagnesNew, self).form_valid(form)

    def form_invalid(self, form, **kwargs):
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(CampagnesNew, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            campagne_list = Campagne.objects.all()
            context['super'] = True
        else:
            campagne_list = Campagne.objects.filter(user_id=self.request.user.id)
        context['campagne_list'] = campagne_list
        context['nb_campagne'] = len(campagne_list)
        context['rayons'] = Rayon.objects.all()
        return context
