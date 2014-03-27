from django.views.generic import FormView
from django.http import HttpResponse
from django.core import serializers

from .models import Person
from .forms import AddPersonForm


class Index(FormView):
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
        if self.request.is_ajax():
            data = serializers.serialize('json', Person.objects.all())
            return HttpResponse(data, mimetype="application/json")
        return super(Index, self).form_valid(form)
