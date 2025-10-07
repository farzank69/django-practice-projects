from django import forms
from . models import Review

#Below is the example of custom forms
# class ReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=100, error_messages={            #By default the required field is set to True.
#         "required": "Your name must not be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=250)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


# Using the ModelForm, we simply make our form connect with models so we don't need to create the custom form fields like we did above.
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"      #to include all the fields from the models.py
        # exclude = ['owner_comment']      #if want to exclude a specific field from the models.
        labels = {
            "user_name": "Your name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "user_name": {
                 "required": "Your name must not be empty!",
                 "max_length": "Please enter a shorter name!"
            }
        }