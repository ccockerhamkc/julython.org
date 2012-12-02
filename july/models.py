"""
Custom User Model for Julython
==============================

This is experimental, but so much worth it!
"""


from django.db import models
from django.contrib.auth.models import AbstractUser

from social_auth.models import UserSocialAuth

from july.people.models import Location, Team

class User(AbstractUser):
    
    location = models.ForeignKey(Location, blank=True, null=True, related_name='location_members')
    team = models.ForeignKey(Team, blank=True, null=True, related_name='team_members')
    
    def add_auth_id(self, auth_str):
        """
        Add a social auth identifier for this user.
        
        The `auth_str` should be in the format '{provider}:{uid}'
        this is useful for adding multiple unique email addresses.
        """
        provider, uid = auth_str.split(':')
        UserSocialAuth.create_social_auth(self, uid, provider)
        
        