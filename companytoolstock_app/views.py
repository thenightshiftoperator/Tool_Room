from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
#Models from toolsdealer_app
from toolroom_app.models import *
from toolsdealer_app.models import *
#Models from CompanytoolStock
from companytoolstock_app.models import *
#Forms from companytoolstock_app
from companytoolstock_app.forms import *
# Create your views here.
def tool_room(request):
    """Main page for TOOL ROOM"""
    return render(request, 'companytoolstock_app/display/tool_room.html')

def tools_stock(request):
    """Main page for TOOLS IN COMPANY STOCK"""
    tool = []

    if Holder.objects.all():
        tool.append('holder')
    if Collet.objects.all():
        tool.append('collet')
    if Tool.objects.all():
        tool.append('tool')
    else:
        context = {}

    context = {'tool': tool}
    return render(request, 'companytoolstock_app/display/tools_stock.html', context)

def display_tools_in_stock(request, type):
    if type == 'holder':
        object_types = []
        objects = Holder.objects.all()
        for object in objects:
            if object.type not in object_types:
                object_types.append(object.type)
            else:
                pass
        context = {'objects': objects, 'object_types': sorted(object_types), 'type': type}

    if type == 'collet':
        object_types = []
        objects = Collet.objects.all()
        for object in objects:
            if object.type not in object_types:
                object_types.append(object.type)
            else:
                pass
        context = {'objects': objects, 'object_types': sorted(object_types), 'type': type}

    if type == 'tool':
        object_types = []
        objects = Tool.objects.all()
        for object in objects:
            if object.type not in object_types:
                object_types.append(object.type)
            else:
                pass
        context = {'objects': objects, 'object_types': sorted(object_types), 'type': type}
    return render(request, 'companytoolstock_app/display/display_tools_in_stock.html', context)

def add_tool(request):
    """Add tools to stock. """
    return render(request, 'companytoolstock_app/display/add_tool.html')

def add_tool_to_stock(request, type):
    """Add Tool to stock."""
    if type == 'holder':
        if request.method != 'POST':
            """No data submitted; create a blank form."""
            form = HolderForm()
        else:
            """POST data submitted; process data."""
            form = HolderForm(request.POST)
            if form.is_valid():
                if Holder.objects.all():
                    adjust_form = form.save(commit=False)
                    if (Holder.objects.filter(type=adjust_form.type).exists() and
                            Holder.objects.filter(bt=adjust_form.bt).exists() and
                            Holder.objects.filter(bt=adjust_form.bt).exists() and
                            Holder.objects.filter(er=adjust_form.er).exists() and
                            Holder.objects.filter(a=adjust_form.a).exists() and
                            Holder.objects.filter(clamp_range=adjust_form.clamp_range).exists()):
                        holder_type = Holder.objects.get(clamp_range=adjust_form.clamp_range)
                        adjust_form.id = holder_type.id
                        adjust_form.quantity += holder_type.quantity
                        adjust_form.save()
                        return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
                    else:
                        form.save()
                        return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
                else:
                    form.save()
                    return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))

        context = {'form': form, 'type': type}


    elif type == 'collet':
        if request.method != 'POST':
            """No data submitted; create a blank form."""
            form = ColletForm()
        else:
            """POST data submitted; process data."""
            form = ColletForm(request.POST)
            if form.is_valid():
                if Collet.objects.all():
                    adjust_form = form.save(commit=False)
                    if (Collet.objects.filter(type=adjust_form.type).exists() and Collet.objects.filter(clamp_range=adjust_form.clamp_range).exists()):
                        collet_type = Collet.objects.get(clamp_range=adjust_form.clamp_range)
                        adjust_form.id = collet_type.id
                        adjust_form.quantity += collet_type.quantity
                        adjust_form.save()
                        return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
                    else:
                        form.save()
                        return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
                else:
                    form.save()
                    return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
            else:
                form.save()
                return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))

        context = {'form': form, 'type': type}
    elif type == 'tool':
        if request.method != 'POST':
            """No data submitted; create a blank form."""
            form = ToolForm()
        else:
            """POST data submitted; process data."""
            form = ToolForm(request.POST)
            if form.is_valid():
                if Tool.objects.all():
                    adjust_form = form.save(commit=False)
                    if (Tool.objects.filter(type=adjust_form.type).exists() and
                     Tool.objects.filter(tool_material_capability=adjust_form.tool_material_capability).exists() and
                     Tool.objects.filter(tool_diameter=adjust_form.tool_diameter).exists() and
                     Tool.objects.filter(corner_radius=adjust_form.corner_radius).exists() and
                     Tool.objects.filter(corner_angle=adjust_form.corner_angle).exists() and
                     Tool.objects.filter(shank_diameter=adjust_form.shank_diameter).exists() and
                     Tool.objects.filter(shank_length=adjust_form.shank_length).exists() and
                     Tool.objects.filter(arbor_diameter=adjust_form.arbor_diameter).exists() and
                     Tool.objects.filter(cutting_length=adjust_form.cutting_length).exists() and
                     Tool.objects.filter(number_of_flutes=adjust_form.number_of_flutes).exists() and
                     Tool.objects.filter(insert_type=adjust_form.insert_type).exists() and
                     Tool.objects.filter(insert_length=adjust_form.insert_length).exists() and
                     Tool.objects.filter(insert_angle=adjust_form.insert_angle).exists() and
                     Tool.objects.filter(tool_total_length=adjust_form.tool_total_length).exists()):
                        tool_type = Tool.objects.get(tool_total_length=adjust_form.tool_total_length)
                        adjust_form.id = tool_type.id
                        adjust_form.quantity += tool_type.quantity
                        adjust_form.save()
                        return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
                    else:
                        form.save()
                        return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
                else:
                    form.save()
                    return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
            else:
                form.save()
                return HttpResponseRedirect(reverse('display_tools_in_stock', args=[type]))
        context = {'form': form, 'type': type}

    return render(request, 'companytoolstock_app/display/add_tool_to_stock.html', context)

def tool_setup(request):
    location = ToolSetUp.objects.all()
    if request.method != 'POST':
        """No data submitted; process data."""
        form = ToolSetUpForm()
    else:
        """POST data submitted; process data."""
        form = ToolSetUpForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tool_room'))

    context = {'form': form}
    return render(request, 'companytoolstock_app/display/tool_setup.html', context)

#AJAX LOADING DROPDOWN MENUS
def load_cells(request):
    sector_id = request.GET.get('sector_id')
    cells = MachinesCell.objects.filter(machines_sector_id=sector_id)
    context = {'cells': cells}
    return render(request, 'companytoolstock_app/dropdown/cells_dropdown.html', context)

def load_machines(request):
    cell_id = request.GET.get('cell_id')
    machines = Machines.objects.filter(machines_cell_id=cell_id).order_by('machine_name')
    context = {'machines': machines}
    return render(request, 'companytoolstock_app/dropdown/machines_dropdown.html', context)

def load_holder_size(request):
    holder_id = request.GET.get('holder_type_id')
    holder = Holder.objects.get(id=holder_id)
    holder_type = Holder.objects.filter(type=holder)
    context = {'holder_type': holder_type}

    return render(request, 'companytoolstock_app/dropdown/holder_dropdown.html', context)

def load_collet_specs(request):
    collet_id = request.GET.get('collet_type_id')
    collet = Collet.objects.get(id=collet_id)
    collet_type = Collet.objects.filter(type=collet)
    context = {'collet_type': collet_type}

    return render(request, 'companytoolstock_app/dropdown/collet_dropdown.html', context)

def load_tool_specs(request):
    tool_id = request.GET.get('tool_type_type')
    tool = Tool.objects.get(id=tool_id)
    tool_type = Tool.objects.filter(type=tool)
    context = {'tool_type': tool_type}

    return render(request, 'companytoolstock_app/dropdown/tool_dropdown.html', context)

def load_tool_diameter(request):
    tool_id = request.GET.get('tool_specs_tool_material_capability')
    print(tool_id)
    tool_type = Tool.objects.filter(tool_material_capability=tool_id)
    context = {'tool_type': tool_type}

    return render(request, 'companytoolstock_app/dropdown/tool_diameter_dropdown.html', context)
