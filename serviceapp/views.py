from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import FeedbackForm
from django.views.generic.list import ListView
from .models import QRCode


class FeedbackView(FormView):
    form_class = FeedbackForm
    template_name = 'serviceapp/serviceapp.html'
    success_url = reverse_lazy('serviceapp:ok')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class QRListView(ListView):
    model = QRCode
