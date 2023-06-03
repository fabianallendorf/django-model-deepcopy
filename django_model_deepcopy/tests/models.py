from django.db import models


class SimpleModel(models.Model):
    text = models.TextField()
