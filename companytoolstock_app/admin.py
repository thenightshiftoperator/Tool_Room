from django.contrib import admin
#MILLING IMPORTS
from companytoolstock_app.models import *
admin.site.register(Holder)
admin.site.register(Collet)
admin.site.register(Tool)

admin.site.register(ToolSetUp)
