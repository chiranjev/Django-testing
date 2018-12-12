# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Posts(models.Model):
    text = models.TextField()

    def __str__(self):
        """A string representation of the model."""
        return self.text