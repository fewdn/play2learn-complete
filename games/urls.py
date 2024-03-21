from django.urls import path

from games.views import (AnagramHuntView, AnagramHuntScoresView, AnagramHuntUserScoresView, 
                         MathFactsView, MathFactsScoresView, MathFactsUserScoresView, 
                         record_anagram_hunt_score, record_math_facts_score)

from pages.views import HomepageView

app_name = 'games'
urlpatterns = [
    path('', HomepageView.as_view()), # homepage route seems like it should be in pages app but VueJS games won't display
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('anagram-hunt-scores/', AnagramHuntScoresView.as_view(), name='anagram-hunt-scores'),
    path('anagram-hunt-user-scores/', AnagramHuntUserScoresView.as_view(), name='anagram-hunt-user-scores'), # try replace with slug for uid
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('math-facts-scores/', MathFactsScoresView.as_view(), name='math-facts-scores'),
    path('math-facts-user-scores/', MathFactsUserScoresView.as_view(), name='math-facts-user-scores'),
    path('record-anagram-hunt-score/', record_anagram_hunt_score, name='record-anagram-hunt-score'),
    path('record-math-facts-score/', record_math_facts_score, name='record-math-facts-score'),
]