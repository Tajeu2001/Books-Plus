from django.contrib import admin
from .models import Profile,Book,Rating


# Register your models here.
admin.site.register(Book)
admin.site.register(Profile)
admin.site.register(Rating)
