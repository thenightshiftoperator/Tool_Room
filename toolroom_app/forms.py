from django import forms

from .models import ToolsStock, MachinesSector, MachinesCell, Machines, MachineToolList

class ToolsStockForm(forms.ModelForm):
    """Creating Page to Allow Tool_Room_administrator insert Tools into Companies Database."""
    class Meta:
        model = ToolsStock
        fields = ['tool_material', 'tool_type', 'tool_diameter', 'tool_cut_length', 'tool_total_length', 'quantity']
        labels = {'tool_material':'tool_material',
        'tool_type':'tool_type',
        'tool_diameter':'tool_diameter',
        'tool_cut_length':'tool_cut_length',
        'tool_total_length':'tool_total_length',
        'quantity':'quantity',
        }

class MachineSectorForm(forms.ModelForm):
    """Creating Page to Register Sector For Production Floor. """
    class Meta:
        model = MachinesSector
        fields = ['sector']
        labels = {'sector': ''}

class CellForm(forms.ModelForm):
    """Creating Page to Register Sector For Production Floor."""
    class Meta:
        model = MachinesCell
        fields = ['cell_name']
        labels = {'cell_name': ''}

    def clean_cell_name(self):
        """Ensuring Cell name is always lower case."""
        return self.cleaned_data['cell_name'].lower()

class MachinesForm(forms.ModelForm):
    """Creating Page to Register Machine in the cell."""
    class Meta:
        model = Machines
        fields = ['machine_name', 'machine_axis_amount', 'machine_z_size', 'machine_x_size', 'machine_y_size', 'machine_magazine_qty']
        labels = {'machine_name': 'machine_name',
            'machine_axis_amount': 'machine_axis_amount',
            'machine_z_size': 'machine_z_size',
            'machine_x_size': 'machine_x_size',
            'machine_y_size': 'machine_y_size',
            'machine_magazine_qty': 'magazine_size',
            }

class MachineToolListForm(forms.ModelForm):
    """Page to allow Cnc_Setter insert Tools into Machine Tool_List"""
    class Meta:
        model = MachineToolList
        fields =['tools', 'tool_number', 'tool_height', 'tool_height_wear', 'tool_radius', 'tool_radius_wear']
        labels = {
        'tools':'Tools',
        'tool_number':'Tool Number',
        'tool_height':'Tool Height',
        'tool_height_wear':'Tool Height Wear',
        'tool_radius':'Tool Radius',
        'tool_radius_wear':'Tool Radius Wear',
        }

#Edit Forms Related to Initial Forms Above
class EditMachinesCellForm(forms.ModelForm):
    """Edit Machine Cell"""
    class Meta:
        model = MachinesCell
        fields = ['cell_name']
        labels = {'cell_name': 'Cell name',}

        def clean_cell_name(self):
            """Ensuring Cell name is always lower case."""
            return self.cleaned_data['cell_name'].lower()

class EditMachineForm(forms.ModelForm):
    """Editing Machine Form."""
    class Meta:
        model = Machines
        fields = ['machine_name', 'machine_axis_amount', 'machine_z_size', 'machine_x_size', 'machine_y_size', 'machine_magazine_qty']
        labels = {'machine_name': 'Machine name',
        'machine_axis_amount': 'Quantity of Axis',
        'machine_z_size': 'Z travel capacity',
        'machine_x_size': 'X travel capacity',
        'machine_y_size': 'y travel capacity',
        'machine_magazine_qty': 'Magazine pockets qty',
        }

class EditMachineToolListForm(forms.ModelForm):
    """Allowing Re-entering and editing tools information in the machine such as type height diameter and wears."""
    class Meta:
        model = MachineToolList
        fields = ['tool_number', 'tool_height', 'tool_height_wear', 'tool_radius', 'tool_radius_wear']
        labels = {
        'tool_number':'Tool Number',
        'tool_height':'Tool Height',
        'tool_height_wear':'Tool Height Wear',
        'tool_radius':'Tool Radius',
        'tool_radius_wear':'Tool Radius Wear',
        }
