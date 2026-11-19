from django.contrib import admin
#MILLING IMPORTS
from toolsdealer_app.models import *

# models for Milling
admin.site.register(FaceMill)
admin.site.register(EndMill)
admin.site.register(BullMill)
admin.site.register(BallMill)
admin.site.register(Tcutter)
admin.site.register(DoveTail)
admin.site.register(Lollipop)
admin.site.register(Engraver)
admin.site.register(ThreadMill)

# models for Drilling
admin.site.register(Drill)
admin.site.register(SpotDrill)
admin.site.register(CenterDrill)
admin.site.register(BoringBar)
admin.site.register(Tap)

# models for Parting tool
admin.site.register(Saw)


# models for Turning
admin.site.register(ExternalTurningTool)
admin.site.register(InternalTurningTool)
admin.site.register(PartingTool)
admin.site.register(ThreadingTool)

# models for holder and collet
admin.site.register(Holder)
admin.site.register(Collet)
