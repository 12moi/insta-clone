

from distutils.command.upload import upload
from email.policy import default
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(max_length=500, default='My Bio', blank=True)
    name = models.CharField(blank=True, max_length=150)
    profile_pic = CloudinaryField('profile_pic')
    location = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return f'{self.user.username}'

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
    
class Image(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=150, blank=True)
    caption = models.CharField('Caption(optional)', max_length=400, blank=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
    upload_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True, )

    class Meta:
        ordering = ["-pk"]

    def get_absolute_url(self):
        return f"/post/{self.id}"

    @property
    def get_all_comments(self):
        return self.comments.all()

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.name} Post'


class Follow(models.Model):
    followers = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.followers} Follow'

class Comments(models.Model):
    comment = models.TextField()
    # post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='comments')
    created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["-comment_date"]


    def __str__(self):
        return f'{self.user.name} Image'
