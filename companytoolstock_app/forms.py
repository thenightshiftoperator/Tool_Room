from django import forms
from toolsdealer_app.models import *
from .models import *

class HolderForm(forms.ModelForm):
    """FORM FOR HOLDER ADDING"""
    class Meta:
        model = Holder
        fields = ['type', 'bt', 'er', 'a', 'clamp_range', 'quantity']

class ColletForm(forms.ModelForm):
    """FORM FOR HOLDER ADDING"""
    class Meta:
        model = Collet
        fields = ['type', 'clamp_range', 'quantity']

class ToolForm(forms.ModelForm):
    """FORM FOR HOLDER ADDING"""
    class Meta:
        model = Tool
        fields = '__all__'

class ToolSetUpForm(forms.ModelForm):
    """TOOL SET UP FORM"""
    class Meta:
        model = ToolSetUp
        fields = ['sector', 'cell', 'machine', 'holder_type', 'holder_specs', 'collet_type', 'collet_specs', 'tool_type', 'tool_specs', 'tool_diameter', 'tool_shoulder_length', 'tool_ohl']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cell'].queryset = MachinesCell.objects.none()
        self.fields['machine'].queryset = Machines.objects.none()
        self.fields['holder_specs'].queryset = Holder.objects.none()
        self.fields['tool_specs'].queryset = Tool.objects.none()
        self.fields['tool_diameter'].queryset = Tool.objects.none()

        if 'sector' in self.data:
            try:
                sector_id = int(self.data.get('sector'))
                self.fields['cell'].queryset = MachinesCell.objects.filter(machines_sector_id=sector_id).order_by('cell_name')
            except(ValueError, TypeError):
                pass

        if 'cell' in self.data:
            try:
                cell_id = int(self.data.get('cell'))
                self.fields['machine'].queryset = Machines.objects.filter(machines_cell_id=cell_id).order_by('machine_name')
            except(ValueError, TypeError):
                pass

        if 'holder_type' in self.data:
            try:
                holder_type = self.data.get('type')
                self.fields['holder_specs'].queryset = Holder.objects.filter(type=holder_type).order_by('type')
            except(ValueError, TypeError):
                pass

        if 'collet_type' in self.data:
            try:
                collet_type = self.data.get('type')
                self.fields['collet_specs'].queryset = Collet.objects.filter(type=collet_type).order_by('type')
            except(ValueError, TypeError):
                pass

        if 'tool_type' in self.data:
            try:
                tool_id = self.data.get('tool_type')
                self.fields['tool_specs'].queryset = Tool.objects.filter(id=tool_id).order_by('id')
            except(ValueError, TypeError):
                pass

        if 'tool_specs' in self.data:
            try:
                tool_specs = self.data.get('tool_specs')
                self.fields['tool_diameter'].queryset = Tool.objects.filter(tool_material_capability=tool_specs).order_by('tool_material_capability')
            except(ValueError, TypeError):
                pass
