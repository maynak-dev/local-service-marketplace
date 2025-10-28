from django.db import models
from users.models import User
from services.models import Service

class Booking(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20, default='pending')  # pending/accepted/completed
    created_at = models.DateTimeField(auto_now_add=True)
