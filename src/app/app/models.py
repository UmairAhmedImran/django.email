from django.db import models

class Email(models.Model):
    email = models.EmailField(max_length=100)