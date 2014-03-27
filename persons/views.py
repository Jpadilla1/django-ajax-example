from django.views.generic import FormView
from django.http import HttpResponse

from .models import Person
from .forms import AddPersonForm
from .mixins import AjaxableResponseMixin


class Index(AjaxableResponseMixin, FormView):
    form_class = AddPersonForm
    success_url = "/"
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        people = Person.objects.all()
        kwargs['people'] = people
        return kwargs

    def form_valid(self, form):
        form.save()
        response = super(AjaxableResponseMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                'first_name': self.request.POST['first_name'],
                'last_name': self.request.POST['last_name']
            }
            return self.render_to_json_response(data)
        else:
            return response
