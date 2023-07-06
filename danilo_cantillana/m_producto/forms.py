from .models import *
from django.forms import *


class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'