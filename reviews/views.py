from datetime import datetime
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Review
# Create your views here.
from .forms import ReviewCreateForm

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    template_name = 'reviews/leave_review.html'
    form_class = ReviewCreateForm
    success_url = reverse_lazy('reviews:thanks')
    
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    #def post(self, request, *args, **kwargs):
    #    now = datetime.now()
    #    review = Review(featured=False, created=now, user=) # explicit but maybe pointless initialize missing ModelForm fields
    #    print(review)
    #    form = ReviewCreateForm(request.POST, instance=review)
    #    if form.is_valid():    # clean / sanitize input and errors
    #        form.save()   
    #        return redirect('reviews:thanks') # After saving to db redirect to thank you page

class ReviewThanksView(TemplateView):
    template_name = 'reviews/thanks.html'
