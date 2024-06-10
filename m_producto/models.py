from django.db.models import *
from django.contrib.auth.models import User


# Create your models here.
def default_foto():
    return 'img/'

class Producto(Model):
    nombre   = CharField(max_length=20, null=False)
    precio   = IntegerField(null=False)
    cantidad = IntegerField(null=False)
    foto     = ImageField(upload_to='img/', null=False, default=default_foto)


