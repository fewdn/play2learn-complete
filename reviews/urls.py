from django.urls import path
from .views import ReviewCreateView, ReviewThanksView

app_name = 'reviews'
urlpatterns = [
    path('create/', ReviewCreateView.as_view(), name='create'),
    path('thanks/', ReviewThanksView.as_view(), name='thanks'),
]