import html
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy

from reviews.models import Review

from common.utils.email import send_email
from .forms import ContactUsForm


# Create your views here.
class AboutUsView(TemplateView):
    template_name = 'pages/about-us.html'


class ContactUsView(FormView):
    template_name = 'pages/contact-us.html'
    form_class = ContactUsForm
    success_url = reverse_lazy('pages:contact-thanks')
    # The view context contains a "form" object with fields of ContactUsForm class

    def form_valid(self, form):
        data = form.cleaned_data
        to = 'you@example.com' #replace this with a target email for contacting you
        subject = 'Play2Learn Contact Us'
        content = f'''<p>Dear Site Admin</p>
                      <p>Contact Form Submitted:</p>
                      <ol>'''
        for key, value in data.items():
            label = key.replace('_', ' ').title()
            entry = html.escape(str(value), quote=False)
            content += f'<li>{label}: {entry}</li>'
        content += '</ol>'

        # Create a SendGrid account and set your Sendgrid key before enabling this
        # "send_email" found in utils/email.py uses the SENDGRID_API_KEY from play2learn/local_settings.py
        # which is imported into play2learn/settings.py
        #
        # send_email(to, subject, content)
        print(content) # Until you create a Sendgrid account you can view the email in the terminal
        return super().form_valid(form)


class ContactUsThanks(TemplateView):
    template_name = 'pages/contact-thanks.html'


class HomepageView(TemplateView):
    template_name = "pages/homepage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.filter(featured=True)
        if reviews.count() > 0:
            context['reviews'] = reviews
        return context
