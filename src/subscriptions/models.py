from django.db import models

# Create your models here.

class Subscription(models.Model):
    name = models.CharField(max_length=120)
    
    class Meta:
        permissions = [
            ("advanced", "Advanced Perm"), # Subscriptions.advanced
            ("pro", "Pro Perm"), # Subscriptions.pro
            ("basic", "Basic Perm"), # Subscriptions.basic
            ("basic_ai", "Basic AI Perm") # Subscriptions.basic_ai
        ]