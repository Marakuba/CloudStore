from django.contrib.auth.models import User as BaseUser
from models import User
from django.db.models.signals import post_save

def create_custom_user(sender, instance, created, **kwargs):
    if created:
        print '-------create_custom_user---------'
        values = {}
        for field in sender._meta.local_fields:
            values[field.attname] = getattr(instance, field.attname)
        user = User(**values)
        user.save()
        
post_save.connect(create_custom_user, BaseUser)    
