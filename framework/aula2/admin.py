# Register your models here.
from django.contrib import admin

from .models import Article
from .models import Reporter

admin.site.register(Article)
admin.site.register(Reporter)