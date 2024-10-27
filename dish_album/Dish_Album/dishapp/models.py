from django.db import models
from accounts.models import Users
from django.utils import timezone
from django.urls import reverse_lazy

class Dishes(models.Model):
    dish_name = models.CharField(max_length=255)
    picture = models.ImageField(null=True, upload_to='picture/')
    comment = models.CharField(max_length=1000)
    shop_name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    user_id = models.ForeignKey(
        Users, on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'dishes'

    def get_absolute_url(self):
        return reverse_lazy('dishapp:dish_home')