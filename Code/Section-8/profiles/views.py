from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from .forms import ProfileForm
from .models import UserProfile
# Create your views here.


# Now the model is handling the file path so no need to save it manually. 
# handle the file upload and store is somewhere.
# def store_file(file):
#     with open("temp/headshot.png", "wb+") as dest:      #Create and open the file
#         for chunk in file.chunks():
#             dest.write(chunk)


class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {
            "form": form
        })
    
    def post(self, request):
        submitted_form  = ProfileForm(request.POST,request.FILES)
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            return HttpResponseRedirect("/profiles")

        return render(request, "profiles/create_profile.html", {
            "form": submitted_form
        })
