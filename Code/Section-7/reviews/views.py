from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView

from . forms import ReviewForm
from . models import Review
# Create your views here.
# Generic View
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, 'reviews/review.html', {
#             'form': form
#         })

#     def post(self, request):
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             form.save()                        
#             return HttpResponseRedirect('/thank-you')

#         return render(request, 'reviews/review.html', {
#             'form': form
#         })


#Create View 

# class ReviewView(CreateView):
#     model = Review
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "/thank-you"



#Form View
class ReviewView(FormView):
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/thank-you"

    def form_valid(self, form):       #Additional method to save the data which has been submitted 
        form.save()
        return super().form_valid(form)
    

#For simple get method view, TemplateView is easy to use.
class ThankYouView(TemplateView):
    template_name = "reviews/thank_you.html"
    #for context it gives different methods.
    def get_context_data(self, **kwargs):
        contex_data = super().get_context_data(**kwargs)      #It's a dictionary
        contex_data["message"] = "This works!"
        return contex_data


# class ReviewListView(TemplateView):
#     template_name = "reviews/review_list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews
#         return context


# ListView will fetch the list data from the model without any unnecessary code
class ReviewListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review            # to point it to the review model

    context_object_name = "reviews"         # write own context name

    # can apply the filters on the data. Example:
    # def get_queryset(self):
    #     query_data = super().get_queryset()
    #     data = query_data.filter(rating__gt=4)
    #     return data

    

# class ReviewDetailView(TemplateView):
#     template_name = "reviews/review_detail.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_data = Review.objects.get(pk=review_id)
#         context["review"] = selected_data
        # return context

#DetailView
class ReviewDetailView(DetailView):
    template_name = "reviews/review_detail.html"
    model = Review          # In the template it will use lowercase 'review' name as a context to provide all the data of the model.
    