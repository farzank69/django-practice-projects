from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from . forms import ReviewForm
from . models import Review
# Create your views here.
# Generic View
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, 'reviews/review.html', {
            'form': form
        })

    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()                        
            return HttpResponseRedirect('/thank-you')

        return render(request, 'reviews/review.html', {
            'form': form
        })

#For simple get method view, TemplateView is easy to use.
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    #for context it gives different methods.
    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)      #It's a dictionary
        contex_data["message"] = "This works!"
        return contex_data


class ReviewListView(TemplateView):
    template_name = "reviews/review_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = Review.objects.all()
        context["reviews"] = reviews
        return context
    

class ReviewDetailView(TemplateView):
    template_name = "reviews/review_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        review_id = kwargs["id"]
        selected_data = Review.objects.get(pk=review_id)
        context["review"] = selected_data
        return context