"""URL for Tool Room"""
from django.urls import path
from . import views

urlpatterns = [
                # COMPANYTOOLSSTOCKE_APP URLS LINKS
    # Home page Main Links in Tool Room
    path('tool_room', views.tool_room, name='tool_room'),

    #Pages for Display of data (TOOL_ROOM) - display_folder
    path('tools_stock', views.tools_stock, name='tools_stock'),

    #Allowing users to insert Data (TOOL_ROOM) - register_folder
    path('add_tool', views.add_tool, name='add_tool'),
    path('add_tool_to_stock/<str:type>', views.add_tool_to_stock, name='add_tool_to_stock'),
    path('display_tools_in_stock/<str:type>', views.display_tools_in_stock, name='display_tools_in_stock'),
    path('tool_setup', views.tool_setup, name='tool_setup'),
    #Allowing users to edit Data (TOOL_ROOM) - edit_folder

    #AJAX URL DROPDOWN FOR TOOLROOM
    path('ajax/load-cells/', views.load_cells, name='ajax_load_cells'), #AJAX
    path('ajax/load-machines/', views.load_machines, name='ajax_load_machines'), #AJAX
    path('ajax/load-holder-size/', views.load_holder_size, name='ajax_load_holder_size'), #AJAX
    path('ajax/load-collet-size/', views.load_collet_specs, name='ajax_load_collet_specs'), #AJAX
    path('ajax/load-tool-specs/', views.load_tool_specs, name='ajax_load_tool_specs'), #AJAX
    path('ajax/load-tool-diameter/', views.load_tool_diameter, name='ajax_load_tool_diameter'), #AJAX
]
