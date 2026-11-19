"""URL for Tool Room"""
from django.urls import path
from companytoolstock_app import views as csviews
from toolsdealer_app import views as tdviews
from . import views

urlpatterns = [
                #  URLS LINKS
    # Home page Main Links in Tool Room
    path('', views.toolroom_main, name='toolroom_main'),
    path('floor_machine_sectors', views.floor_machine_sectors, name='floor_machine_sectors'),

    #Pages for Display of data (Production floor skeleton II) - display_folder
    path('floor_machine_sectors/<int:sector_id>', views.machine_cells, name='machine_cells'),
    path('machine_cells/<int:cell_id>', views.machines, name='machines'),
    path('machines/<int:machine_id>', views.machine, name='machine'),
    path('machine/<int:machine_id>', views.machine_tool_list, name='machine_tool_list'),
    path('tools_requests', views.tools_requests, name='tools_requests'),

    path('register_sector/', views.register_sector, name='register_sector'),
    path('register_machine_cell/<int:machine_sector_id>', views.register_machine_cell, name='register_machine_cell'),
    path('register_machine/<int:machine_cell_id>', views.register_machine, name='register_machine'),
    path('register_tools_into_stock', views.register_tools_into_stock, name='register_tools_into_stock'),
    path('register_machine_tool_list/<int:machine_id>', views.register_machine_tool_list, name='register_machine_tool_list'),

    #Allowing users to edit Data (Production floor skeleton II) - edit_folder
    path('edit_machine_cell/<int:cell_id>', views.edit_machine_cell, name='edit_machine_cell'),
    path('edit_machine/<int:machine_id>', views.edit_machine, name='edit_machine'),
    path('edit_tool_from_machine_tool_list/<int:tool_id><int:machine_id>', views.edit_tool_from_machine_tool_list, name='edit_tool_from_machine_tool_list'),

]
