from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.admin import site

from DjangoTestApp.models import *

import os

admin.site.unregister(Group)
admin.site.unregister(User)


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)


class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author')

admin.site.register(Post, PostAdmin)
