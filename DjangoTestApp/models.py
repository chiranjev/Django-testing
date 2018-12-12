from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class CustomUser(User):

    def save(self, *args, **kwargs):
        if self.pk == None:
            self.set_password(self.password)
        super(CustomUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Custom User"
        verbose_name_plural = "Custom Users"


class Post(models.Model):

    title = models.CharField(max_length=100)

    content = models.TextField(null=True, blank=True)

    author = models.ForeignKey('CustomUser', on_delete=models.CASCADE)

    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "MyBlog"
        verbose_name_plural = "MyBlog"