from django.forms import ModelForm
from main_app.models import ShoppingGuide

class ShoppingGuideForm(ModelForm):
    class Meta:
        model = ShoppingGuide
        fields = '__all__'