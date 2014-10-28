from django.views.generic import TemplateView

from tests.models import TestCaseExecution

# Create your views here.
class TestView(TemplateView):
    template_name = "tests/index.html"

    def get_context_data(self, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        test_case_exec = TestCaseExecution.objects.all()
        context['test_case_exec'] = test_case_exec
        context['test_case_exec_fields'] = TestCaseExecution._meta.get_all_field_names()
        return context
