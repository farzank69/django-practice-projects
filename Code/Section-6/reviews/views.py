from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.

def review(request):
    if request.method == "POST":
        extract_data = request.POST["username"]
        print(extract_data)
        return HttpResponseRedirect('/thank-you')
    
    return render(request, 'reviews/review.html')


def thank_you(request):
    return render(request, 'reviews/thank_you.html')