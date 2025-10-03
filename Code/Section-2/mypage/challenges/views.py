from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    'january': "This is the january challenge page.",
    'february': "Hello, world. This is for the february month.",
    'march': "March Challenge: Learn about Django.",
    'april': "April Challenge: Learn about React.",
    'may': "May Challenge: Learn about Vue.",
    'june': "June Challenge: Learn about Angular.",
    'july': "July Challenge: Learn about Svelte.",
    'august': "August Challenge: Learn about Flask.",
    'september': "September Challenge: Learn about FastAPI.",
    'october': "October Challenge: Learn about Docker.",
    'november': "November Challenge: Learn about Kubernetes.",
    'december': None
}

def index(request):
    months = list(monthly_challenges.keys())
    
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,  month):
    try:
        # capitalized_month = month.capitalize()     # Not needed if using template filters (title)
        challenge_text = monthly_challenges[month]
        return render(request,"challenges/challenge.html", {
            "text": challenge_text, 
            "month": month
            })
    
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")