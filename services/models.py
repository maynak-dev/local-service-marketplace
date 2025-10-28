from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Service(models.Model):
    CATEGORY_CHOICES = [
        ('electrician', 'Electrician'),
        ('plumber', 'Plumber'),
        ('tutor', 'Tutor'),
        ('carpenter', 'Carpenter'),
    ]
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='services')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=8, decimal_places=2)
    latitude = models.FloatField()
    longitude = models.FloatField()
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
