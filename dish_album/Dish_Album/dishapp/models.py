from django.db import models
from accounts.models import Users
from django.utils import timezone
from django.urls import reverse_lazy
from django.core.exceptions import ValidationError
import os

def validate_image_file(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    if not ext.lower() in valid_extensions:
        raise ValidationError('画像は指定された拡張子のファイルしか登録できません。: jpg, jpeg, png, gif')

class Dishes(models.Model):
    dish_name = models.CharField(max_length=255)
    picture = models.FileField(null=True, upload_to='picture/', validators=[validate_image_file])
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