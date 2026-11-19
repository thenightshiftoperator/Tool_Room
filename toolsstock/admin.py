from django.contrib import admin

# Register your models here.
from toolsstock.models import *
admin.site.register(Holder)
admin.site.register(Collet)
admin.site.register(Tool)
