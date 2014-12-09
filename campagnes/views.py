from datetime import timedelta, datetime

from django import forms
from django.views.generic import TemplateView, FormView
from mptt import forms as mptt_forms

from campagnes.models import Campagne, PlanificationCampagne, Rayon, Enseigne, Magasin


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
    annonceur = forms.CharField()
    enseignes = forms.ModelMultipleChoiceField(queryset=Enseigne.objects.all(),
                                               widget=forms.CheckboxSelectMultiple)
    rayons = mptt_forms.TreeNodeMultipleChoiceField(queryset=Rayon.objects.all(),
                                                    widget=forms.CheckboxSelectMultiple,
                                                    level_indicator=u'')
    date_debut = forms.DateField()
    date_fin = forms.DateField()

    def clean(self):
        if all(x in self.cleaned_data for x in ['date_debut', 'date_fin']) \
                and self.cleaned_data['date_debut'] > self.cleaned_data['date_fin']:
            raise forms.ValidationError('La date de fin ne doit pas preceder '
                                        'la date de debut, ici %s > %s'
                                        % (self.cleaned_data['date_debut'], self.cleaned_data['date_fin']))
        return super(CampagnesNewForm, self).clean()


class CampagnesNew(FormView):
    template_name = "campagnes/nouvelle_campagne.html"
    form_class = CampagnesNewForm
    success_url = '/campagnes/'

    def form_valid(self, form):
        # Create the campagne
        campagne = Campagne.objects.create(nom=form.cleaned_data['nom'],
                                           annonceur=form.cleaned_data['annonceur'],
                                           user=self.request.user,
                                           date_debut=form.cleaned_data['date_debut'],
                                           date_fin=form.cleaned_data['date_fin'])

        # Creating the tests, get ready for the cascade
        # In the date range
        for date in self.daterange(form.cleaned_data['date_debut'], form.cleaned_data['date_fin']):
            # For all enseignes
            for enseigne in form.cleaned_data['enseignes']:
                # In all Magasins
                for magasin in Magasin.objects.filter(enseigne=enseigne.id):
                    # In all rayons
                    for rayon in form.cleaned_data['rayons']:
                        # The hour of execution
                        exec_hour = 10
                        exec_timestamp = datetime(date.year, date.month, date.day, exec_hour)
                        PlanificationCampagne.objects.create(campagne=campagne,
                                                             date_execution=exec_timestamp,
                                                             rayon=rayon,
                                                             magasin=magasin,
                                                             status='WAIT')
    
        return super(CampagnesNew, self).form_valid(form)

    @staticmethod
    def daterange(start_date, end_date):
        # Increase end_date by one to inclue it in range
        end_date += timedelta(days=1)
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)

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


class ScreenshotsView(TemplateView):
    template_name = 'campagnes/screenshots.html'

    def get_context_data(self, **kwargs):
        context = super(ScreenshotsView, self).get_context_data(**kwargs)
        if self.request.user.is_superuser:
            campagne_list = Campagne.objects.all()
            context['super'] = True
        else:
            campagne_list = Campagne.objects.filter(user_id=self.request.user.id)
        context['campagne_list'] = campagne_list
        context['nb_campagne'] = len(campagne_list)
        context['rayons'] = Rayon.objects.all()
        context['tests'] = PlanificationCampagne.objects.exclude(screenshot="").filter(campagne__in=campagne_list)
        return context
