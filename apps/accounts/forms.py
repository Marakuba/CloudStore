# -*- coding: utf-8 -*-
from django.contrib.auth.forms import UserChangeForm
from models import User as CustomUser


class CustomUserChangeForm(UserChangeForm):
    #....
    class Meta:
        model = CustomUser
