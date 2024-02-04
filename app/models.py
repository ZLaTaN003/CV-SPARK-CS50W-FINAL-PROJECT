from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Section(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class User(AbstractUser):
 sections = models.ManyToManyField(Section, related_name='members', blank=True)


class Candidate(models.Model):
  user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='user_candidate')
  name = models.CharField(max_length=200)
  email = models.CharField(max_length=200)
  phone = models.CharField(max_length=50)
  about = models.TextField(max_length=3000)
  skills = models.TextField(max_length=3000)
  degree = models.CharField(max_length=200)
  university = models.CharField(max_length=200)
  experience = models.TextField(max_length=2000)
  
  def __str__(self):
      return f"{self.user} on {self.name}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='userprofile')
    bio = models.TextField(blank=True)
    birthdate = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True,default='profilepic.jpg')

    def __str__(self):
        return f"{self.user} Profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.get_or_create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cv = models.ForeignKey(Candidate, on_delete=models.CASCADE)




