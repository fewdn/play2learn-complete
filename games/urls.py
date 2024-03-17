from django.urls import path

from games.views import MathFactsView, AnagramHuntView #,HomepageView
from pages.views import HomepageView

app_name = 'games'
urlpatterns = [
    path('', HomepageView.as_view()), # oddly trying to move homepage route outside of games/urls.py will not display VueJS games
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
]