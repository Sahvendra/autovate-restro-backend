from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=True, null=True)
    likes = models.PositiveIntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    views = models.PositiveIntegerField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    serving_size = models.CharField(max_length=255, blank=True, null=True)
    prep_time = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ingredients = models.JSONField(blank=True, null=True)
    nutrition = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name or "Unnamed Category"


class MenuListItem(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    pre_piece = models.PositiveIntegerField(blank=True, null=True)
    likes = models.PositiveIntegerField(blank=True, null=True)
    views = models.PositiveIntegerField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    preTime = models.CharField(max_length=50, blank=True, null=True)
    deliveryFee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ingredients = models.JSONField(blank=True, null=True)
    nutrients = models.JSONField(blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True)
    image = models.URLField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name or "Unnamed Item"