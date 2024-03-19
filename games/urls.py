from django.urls import path

from games.views import AnagramHuntView, AnagramHuntScoresView, AnagramHuntUserScoresView, MathFactsView, MathFactsScoresView, MathFactsUserScoresView
from pages.views import HomepageView

app_name = 'games'
urlpatterns = [
    path('', HomepageView.as_view()), # homepage route seems like it should be in pages app but VueJS games won't display
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('games/anagram-hunt-scores/', AnagramHuntScoresView.as_view(), name='anagram-hunt-scores'),
    path('games/anagram-hunt-user-scores/', AnagramHuntUserScoresView.as_view(), name='anagram-hunt-user-scores'), # try replace with slug for uid
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('games/math-facts-scores', MathFactsScoresView.as_view(), name='math-facts-scores'),
    path('math-facts-scores/', MathFactsUserScoresView.as_view(), name='math-facts-user-scores'),
]