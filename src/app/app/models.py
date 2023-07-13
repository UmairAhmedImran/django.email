from django.db import models

class email(models.Model):
    email = models.EmailField(max_length=100)