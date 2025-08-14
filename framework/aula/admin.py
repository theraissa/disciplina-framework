# Register your models here.
from django.contrib import admin

from .models import Passaporte
from .models import Pessoa

admin.site.register(Passaporte)
admin.site.register(Pessoa)

