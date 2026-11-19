from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('toolroom_app.urls'), name='toolroom_app'),
    path('', include('companytoolstock_app.urls'), name='companytoolstock_app'),
    path('', include('toolsdealer_app.urls'), name='toolsdealer_app'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
