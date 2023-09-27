from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Relic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    best_rarity = models.CharField(max_length=255)
    ideal_main_stat = models.CharField(max_length=255)
    ideal_variant_amount = models.IntegerField()
