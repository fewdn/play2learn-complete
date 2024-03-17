from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from .forms import ContactUsForm

# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'pages/about-us.html'

class ContactUsView(FormView):
    template_name = 'pages/contact-us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('pages:contact-thanks')
    # The view context contains a "form" object with fields of ContactUsForm class

class ContactUsThanks(TemplateView):
    template_name = 'pages/contact-thanks.html'
