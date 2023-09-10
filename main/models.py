from django.db import models

# Create your models here.
class Relic(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    best_rarity = models.CharField(max_length=255)
    ideal_main_stat = models.CharField(max_length=255)
    ideal_variant_amount = models.IntegerField()