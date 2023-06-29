from .models import *
from django.forms import *

class Int_Producto(ModelForm):
    class Meta:
        model = Producto
        fields = ['titulo','detalle']