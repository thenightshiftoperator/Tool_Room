"""URL for Tools dealer App"""
from django.urls import path
from . import views

urlpatterns = [
                #TOOLSDEALER_APP URLS LINKS
    #Pages for Display Catalogue Header divisions
    path('seller_catalogue', views.seller_catalogue, name='seller_catalogue'),
    #Pages for Display Catalogue sub-Header divisions
    path('tools/<str:toolname>', views.tools, name='tools'),
    #Pages for Display Catalogue sub-Header divisions
    path('tool/<str:toolname>\<str:name>', views.tool, name='tool'),
    #Pages for Display Catalogue sub-Header divisions
    #Deleting Information from database (TOOL_ROOM)
]
