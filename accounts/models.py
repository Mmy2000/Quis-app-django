from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    image = models.ImageField(upload_to='users/')
    about = models.TextField(max_length=4000 , blank=True , null=True)
    country = models.CharField(max_length=50 ,blank=True, null=True)


    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
    def full_address(self):
        return f"{self.country} | {self.city} "


    def __str__(self):
        return str(self.user)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

