from datetime import datetime
from django.shortcuts import redirect
from django.views.generic import FormView, TemplateView, CreateView

from .models import Review
# Create your views here.
from .forms import ReviewCreateForm

class ReviewCreateView(CreateView):
    model = Review
    template_name = 'reviews/leave_review.html'
    form_class = ReviewCreateForm

    def post(self, request, *args, **kwargs):
        now = datetime.now()
        review = Review(featured=False, created=now) # explicit but maybe pointless initialize missing ModelForm fields
        form = ReviewCreateForm(request.POST, instance=review)
        if form.is_valid():    # clean / sanitize input and errors
            form.save()   
            return redirect('reviews:thanks') # After saving to db redirect to thank you page

class ReviewThanksView(TemplateView):
    template_name = 'reviews/thanks.html'
