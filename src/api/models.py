from django.utils import timezone
from django.db import models

# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     likes = models.PositiveIntegerField()
#     rating = models.FloatField()
#     views = models.PositiveIntegerField()
#     image = models.URLField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     serving_size = models.CharField(max_length=255)
#     prep_time = models.CharField(max_length=50)
#     description = models.TextField()
#     ingredients = models.JSONField()
#     nutrition = models.JSONField()

#     def __str__(self):
#         return self.name




class Category(models.Model):
    name = models.CharField(max_length=255)
    likes = models.PositiveIntegerField()
    rating = models.FloatField()
    views = models.PositiveIntegerField()
    image = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    serving_size = models.CharField(max_length=255)
    prep_time = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.JSONField()
    nutrition = models.JSONField()
    servingSize = models.CharField(max_length=255, null=True, blank=True)
    prepTime = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

# class MenuListItem(models.Model):
#     name = models.CharField(max_length=255)
#     category = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     pre_piece = models.PositiveIntegerField()
#     likes = models.PositiveIntegerField()
#     views = models.PositiveIntegerField()
#     rating = models.FloatField()
#     pre_time = models.CharField(max_length=50)
#     delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
#     description = models.TextField()
#     ingredients = models.JSONField()
#     nutrients = models.JSONField()
#     quantity = models.PositiveIntegerField(default=0)
#     image = models.URLField()

#     def __str__(self):
#         return self.name




class MenuListItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pre_piece = models.PositiveIntegerField()
    likes = models.PositiveIntegerField()
    views = models.PositiveIntegerField()
    rating = models.FloatField()
    preTime = models.CharField(max_length=50)  # Updated for "preTime"
    # delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)  # Updated for "deliveryFee"
    description = models.TextField()
    ingredients = models.JSONField()
    nutrients = models.JSONField()
    quantity = models.PositiveIntegerField(default=0)
    image = models.URLField()

    def __str__(self):
        return self.name

# class Orders(models.Model):
#     dish_name=models.CharField(max_length=50)
#     price=models.IntegerField()
#     name=models.CharField(max_length=50)
#     table_number=models.IntegerField()
    
class Orders (models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('preparing', 'Preparing'),
        ('on_way', 'On the Way'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled')
    ]

    user_name=models.CharField(max_length=50,blank=True)
    dish=models.CharField(max_length=50,blank=True)
    quantity =models.IntegerField(default=1,blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    
    ordered_at = models.DateTimeField(default=timezone.now)
    # delivery_address = models.TextField()
    delivery_address = models.TextField(null=True, blank=True) 
    payment_status = models.BooleanField(default=False)
    table_number=models.IntegerField()
    image = models.URLField()

    def __str__(self):
        return f"Order #{self.id} - {self.dish} x{self.quantity} for {self.user_name}"