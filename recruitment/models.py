from django.db import models
from django.conf import settings 
from django.utils import timezone

class Applicant(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email_address = models.EmailField(max_length=255)
    gender = models.CharField(max_length=1,
                                choices=[
                                            ('M','Male'),
                                            ('F','Female'),
                                            ('O','Other'),
                                        ]
                            )

