from django.contrib import admin
from .models import Tag, Startup, NewsLink

# Register your models here.

admin.site.register([Tag, Startup, NewsLink])

