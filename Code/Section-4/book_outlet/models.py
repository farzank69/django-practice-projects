from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=80)
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Countries"  # Change the plural name in the admin interface from "Countrys" to "Countries"

class Address(models.Model):
    street = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.postal_code} {self.city}"

    class Meta:   # Meta is a nested class that provides metadata to the model and it is used to change the behavior of the model.
        verbose_name_plural = "Address Entries" # Change the plural name in the admin interface from "Addresss" to "Address Entries"    
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True) # If address is deleted, delete the author too.  

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True) # If author is deleted, delete all their books too.  
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True) # SlugField is used to create SEO friendly URLs, it is a short label for something containing only letters, numbers, underscores or hyphens.
    # Also can set slug as primary key by adding primary_key=True in the field.
    published_countries = models.ManyToManyField(Country) # A book can be published in multiple countries and a country can have multiple books published in it.

    def get_absolute_url(self):         # get_absolute_url is a conventional name and is used to get the URL of an object
        return reverse("book_detail", args=[self.slug]) 
    
    # Overriding the save method to automatically generate slug from title
    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)  # Automatically generate slug from title
    #     super().save(*args, **kwargs)  # Call the "real" save() method.
    # Removed save method to use prepopulated_fields in admin.py instead. otherwise slug will be overwritten on every save.
    def __str__(self):
        return f"{self.title} ({self.rating})"