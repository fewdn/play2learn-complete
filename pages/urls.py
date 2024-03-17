from django.urls import path

from pages.views import AboutUsView, ContactUsView, ContactUsThanks

app_name = "pages"

urlpatterns = [
    path('about-us/', AboutUsView.as_view(), name="about-us"),
    path('contact-us/', ContactUsView.as_view(), name="contact-us"),
    path('contact-thanks/', ContactUsThanks.as_view(), name="contact-thanks"),
]