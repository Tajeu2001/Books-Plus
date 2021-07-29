from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
import datetime as dt


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_picture = CloudinaryField('image')
    bio = models.TextField(max_length=500, default="My Bio", blank=True)
    contact = models.CharField(blank=True, max_length=120)
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.user

    def delete_profile(self):
        self.delete()

    @classmethod
    def search_profile(cls, name):
        return cls.objects.filter(user__username__icontains=name).all()


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models. CharField(max_length=500)
    author = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    publisher = models.CharField(max_length=200)
    cover = CloudinaryField('image')
    pdf = CloudinaryField('PDF')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    def __str__(self):
        return self.title


    @classmethod
    def search_book(cls,search_term):
        books = Book.objects.filter(title__icontains=search_term).all()
        return books

class Rating(models.Model):
    rating = (1, 1),(2, 2),(3, 3),(4, 4),(5, 5),(6, 6),(7, 7),(8, 8),(9, 9),(10, 10)

    design = models.IntegerField(choices=rating,blank=True,default=0)
    usability = models.IntegerField(choices=rating, blank=True,default=0)
    content = models.IntegerField(choices=rating, blank=True,default=0)
    overall_score = models.IntegerField(blank=True,default=0)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return f'{self.book.title} ratings'
