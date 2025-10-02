from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
    list_items = ""
    months = list(monthly_challenges.keys())
    
    for month in months:
        capitalized_month = month.capitalize()
        path = reverse('month-challenge', args=[month])
        list_items += f"<li><a href=\"{path}\">{capitalized_month}</a></li>"
       
    response_data = f"<ul> {list_items} </ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month!")
    
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,  month):
    try:
        challenges_text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenge.html")
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")