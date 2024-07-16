from django.db import models

# Create your models here.
class PageVisit(models.Model):
    # db -> table -> PageVisit
    # id -> primary key -> auto field -> 1,2,3,4....
    path = models.TextField(blank=True, null=True) # col
    timestamp = models.DateTimeField(auto_now_add=True) # col