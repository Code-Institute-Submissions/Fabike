# some of the code was copied from Boutique Ado project's repository
# and modified according to the project's needs
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class Profile(models.Model):
    """
    User Profile model is used for maintaining default
    delivery information and storing order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_phone_number = models.CharField(max_length=20,
                                         null=True, blank=True)
    user_address_line1 = models.CharField(max_length=60,
                                          null=True, blank=True)
    user_address_line2 = models.CharField(max_length=60,
                                          null=True, blank=True)
    user_town_or_city = models.CharField(max_length=50,
                                         null=True, blank=True)
    user_county = models.CharField(max_length=50,
                                   null=True, blank=True)
    user_postcode = models.CharField(max_length=20,
                                     null=True, blank=True)
    user_country = CountryField(blank_label='Country',
                                null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    """
    Create or update user Profile when User object is created
    """
    if created:
        Profile.objects.create(user=instance)
    # Existing users: just save the profile
    instance.profile.save()
