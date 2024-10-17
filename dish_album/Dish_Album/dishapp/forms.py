from django import forms
from .models import Dishes

class DishCreateForm(forms.ModelForm):
    dish_name = forms.CharField(label='料理名')
    shop_name = forms.CharField(label='店名')
    price = forms.IntegerField(label='価格')
    comment = forms.CharField(label='一言コメント')
    picture = forms.FileField(label='料理画像', required=False)
    
    class Meta:
        model = Dishes
        fields = ['dish_name', 'shop_name', 'price', 'comment', 'picture']

class DishUpdateForm(forms.ModelForm):

    class Meta:
        model = Dishes
        fields = ['dish_name', 'shop_name', 'price', 'comment', 'picture']