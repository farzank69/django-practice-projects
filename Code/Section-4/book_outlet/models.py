from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=50)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # SlugField is used to create SEO friendly URLs, it is a short label for something containing only letters, numbers, underscores or hyphens.
    # Also can set slug as primary key by adding primary_key=True in the field.

    def get_absolute_url(self):         # get_absolute_url is a conventional name and is used to get the URL of an object
        return reverse("book_detail", args=[self.slug]) 
    
    # Overriding the save method to automatically generate slug from title
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)  # Automatically generate slug from title
    #     super().save(*args, **kwargs)  # Call the "real" save() method.
    # Removed save method to use prepopulated_fields in admin.py instead. otherwise slug will be overwritten on every save.
    def __str__(self):
        return f"{self.title} ({self.rating})"