from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

#Models Import
from .models import *
#Form Import
from .forms import *

# Views for Data display (Production floor skeleton II) - display_folder
def toolroom_main(request):
    """The home page for Tools Room."""
    return render(request, 'toolroom_app/display/toolroom_main.html')

def floor_machine_sectors(request):
    """Floor Distribuition of cells/sectors."""
    floor_sectors = MachinesSector.objects.all()
    context = {'floor_sectors': floor_sectors}
    return render(request, 'toolroom_app/display/floor_machine_sectors.html', context)

def machine_cells(request, sector_id):
    """Display Cells."""
    machine_sector = MachinesSector.objects.get(id=sector_id)
    cells = machine_sector.registercell_set.all()
    context = {'machine_sector': machine_sector, 'cells': cells }
    return render(request, 'toolroom_app/display/machine_cells.html', context)

def machines(request, cell_id):
    """Display Machines in the cell selected."""
    cell = MachinesCell.objects.get(id=cell_id)
    machines = cell.registermachines_set.all()

    context = {'cell': cell, 'machines': machines}
    return render(request, 'toolroom_app/display/machines.html', context)

def machine(request, machine_id):
    """Page Display for machine information and access to tool_list, current_job, future_job"""
    machine = Machines.objects.get(id=machine_id)
    context = {'machine':machine}
    return render(request, 'toolroom_app/display/machine.html', context)

def machine_tool_list(request, machine_id,):
    machine = Machines.objects.get(id=machine_id)
    machinetoollist = machine.machinetoollist_set.all()
    magazine = []

    for number in range(machine.machine_magazine_qty + 1):
        magazine.append(number)


    context = {'machine': machine, 'machinetoollist': machinetoollist, 'magazine': magazine}
    return render(request, 'toolroom_app/display/machine_tool_list.html', context)

def tools_requests(request):
    """Display tools requested by the CNC Setters. """

    return render(request, 'toolroom_app/display/tools_requests.html')

# Views Allowing User to Input/Register main data (Production floor skeleton II) - register_folder
def register_tools_into_stock(request):
    """Page to allow toom_room_manager insert tools into stock"""

    if request.method != 'POST':
        """Create a clean form to insert data."""
        form = ToolsStockForm()
    else:
        """POST data from form to database."""
        form = ToolsStockForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tools_stock'))

    context = {'form': form}
    return render(request, 'toolroom_app/register/register_tools_into_stock.html', context)

def register_sector(request):
    """Let user add Sector in Shop Floor."""
    current_sectors = MachinesSector.objects.all()

    if request.method != 'POST':
        """No data submitted; create a blank form."""
        form = MachineSectorForm()
    else:
        """POST data submitted; process data."""
        form = MachineSectorForm(request.POST)
        if form.is_valid():
            if current_sectors.filter(sector=form.cleaned_data['sector']).exists():
                messages.error(request, form.cleaned_data['sector'] + ' Sector already exists')
            else:
                form.save()
                return HttpResponseRedirect(reverse('floor_machine_sectors'))

    context = {'form': form}
    return render(request, 'toolroom_app/register/register_sector.html', context)

def register_machine_cell(request, machine_sector_id):
    machine_sector = MachinesSector.objects.get(id=machine_sector_id)
    cell_names = machine_sector.registercell_set.all()

    if request.method != 'POST':
        """No data submitted; process data."""
        form = CellForm()
    else:
        """POST data submitted; process data."""
        form = CellForm(data=request.POST)
        if form.is_valid():
            if machine_sector and cell_names.filter(cell_name=form.cleaned_data['cell_name']).exists():
                messages.error(request, form.cleaned_data['cell_name'] + ' ' + str(machine_sector) + ' - already exists')
            else:
                new_cell = form.save(commit=False)
                new_cell.machines_sector = machine_sector
                new_cell.save()
                return HttpResponseRedirect(reverse('machine_cells', args=[machine_sector_id]))

    context = {'form': form, 'machine_sector': machine_sector}
    return render(request, 'toolroom_app/register/register_cell.html', context)

def register_machine(request, machine_cell_id):
    """Let user/managers register machines in the workflow."""
    machine_cell = MachinesCell.objects.get(id=machine_cell_id)
    machine_name = machine_cell.registermachines_set.all()

    if request.method != 'POST':
        """No data submitted; process data."""
        form = MachinesForm()
    else:
        """POST data submitted; process data."""
        form = MachinesForm(data=request.POST)
        if form.is_valid():
            if machine_name.filter(machine_name=form.cleaned_data['machine_name']).exists():
                messages.error(request, form.cleaned_data['machine_name'] + ' in ' + str(machine_cell.cell_name) + ' - already exists')
            else:
                new_machine = form.save(commit=False)
                new_machine.machines_cell = machine_cell
                new_machine.save()
                return HttpResponseRedirect(reverse('machines', args=[machine_cell_id]))

    context = {'machine_cell': machine_cell,'form': form}
    return render(request, 'toolroom_app/register/register_machine.html', context)

def register_machine_tool_list(request, machine_id):
    """Let Cnc_Setter Create and Set tools to a specified machine. """
    machine = Machines.objects.get(id=machine_id)
    machine_tool_list = machine.machinetoollist_set.all()

    if request.method != 'POST':
        """Clean Form for data input"""
        form = MachineToolListForm()
    else:
        """Process Data inputed in the clean form."""
        form = MachineToolListForm(data=request.POST)
        if form.is_valid():
            print(machine_tool_list.filter(tool_number=form.cleaned_data['tool_number']).exists())
            if int(form.cleaned_data['tool_number']) > int(machine.machine_magazine_qty):
                messages.error(request, 'Machine magazine handles ' + str(machine.machine_magazine_qty) + ' tools only, please select a tool number under the limit.')
            elif machine_tool_list.filter(tool_number=form.cleaned_data['tool_number']).exists():
                messages.error(request, 'Magazine pocket ' + str(form.cleaned_data['tool_number']) + ' is already full')
            elif machine_tool_list.filter(tools=form.cleaned_data['tools'].id).exists():
                messages.error(request, form.cleaned_data['tools'].tool_type + ' ' + form.cleaned_data['tools'].tool_diameter + 'Ø is already in the magazine')
            else:
                specify_machine = form.save(commit=False)
                specify_machine.machine = machine
                specify_machine.save()
                return HttpResponseRedirect(reverse('machine_tool_list', args=[machine_id]))


    context = {'form': form, 'machine': machine}
    return render(request, 'toolroom_app/register/register_machine_tool_list.html', context)


# Views for Allowing User Edit data  (Production floor skeleton II) - edit_folder
def edit_machine_cell(request, cell_id):
    cell = MachinesCell.objects.get(id=cell_id)
    sector_id = cell.machines_sector.id
    sector = MachinesSector.objects.get(id=sector_id)
    cell_list = sector.registercell_set.all()
    current_cell = sector.registercell_set.get(id=cell_id)

    if request.method != 'POST':
        """Import Data from registered cell to be updated."""
        form = EditMachinesCellForm(instance=cell)
    else:
        form = EditMachinesCellForm(instance=cell, data=request.POST)
        if form.is_valid():
            if cell_list.filter(cell_name=form.cleaned_data['cell_name']).exists():
                if current_cell.cell_name == form.cleaned_data['cell_name']:
                    return HttpResponseRedirect(reverse('machines', args=[cell_id]))
                else:
                    messages.error(request, form.cleaned_data['cell_name'] + ' ' + str(sector.sector) + ' - already exists')
            else:
                adjust_form = form.save(commit=False)
                adjust_form.machines_sector = cell.machines_sector
                adjust_form.save()
                return HttpResponseRedirect(reverse('machines', args=[cell_id]))

    context = {'form': form, 'current_cell': current_cell, 'cell': cell}
    return render(request, 'toolroom_app/edit/edit_machine_cell.html', context)

def edit_machine(request, machine_id):
    machine = Machines.objects.get(id=machine_id)
    machine_cell = machine.machines_cell.id
    cell = MachinesCell.objects.get(id=machine_cell)
    cell_machines_list = cell.registermachines_set.all()
    current_machine = cell.registermachines_set.get(id=machine_id)

    if request.method != 'POST':
        form = EditMachineForm(instance=machine)
    else:
        form = EditMachineForm(data=request.POST, instance=machine)
        if form.is_valid():
            if cell_machines_list.filter(machine_name=form.cleaned_data['machine_name']).exists():
                if current_machine.machine_name == form.cleaned_data['machine_name']:
                    return HttpResponseRedirect(reverse('machine', args=[machine_id]))
                else:
                    messages.error(request, form.cleaned_data['machine_name'] +' - already exists')
            else:
                adjust_form = form.save(commit=False)
                adjust_form.machines_cell = machine.machines_cell
                form.save()
                return HttpResponseRedirect(reverse('machine', args=[machine_id]))

    context = {'form': form, 'machine':machine}
    return render(request, 'toolroom_app/edit/edit_machine.html', context)

def edit_tool_from_machine_tool_list(request, tool_id, machine_id):
    machine = Machines.objects.get(id=machine_id)
    machine_tool_list = machine.machinetoollist_set.all()
    machine_tool = machine.machinetoollist_set.get(id=tool_id)

    if request.method != 'POST':
        """Clean Form for data input"""
        form = EditMachineToolListForm(instance=machine_tool)
    else:
        """Process Data inputed in the clean form."""
        form = EditMachineToolListForm(data=request.POST)
        if form.is_valid():
            if int(form.cleaned_data['tool_number']) > int(machine.machine_magazine_qty):
                    messages.error(request, 'Machine magazine handles ' + str(machine.machine_magazine_qty) + ' tools only, please select a tool number under the limit.')
            elif machine_tool_list.filter(tool_number=form.cleaned_data['tool_number']).exists():
                if machine_tool.tool_number == form.cleaned_data['tool_number']:
                    adjust_form = form.save(commit=False)
                    machine_tool.delete()
                    adjust_form.machine = machine
                    adjust_form.tools = machine_tool.tools
                    adjust_form.save()
                    return HttpResponseRedirect(reverse('machine_tool_list', args=[machine_id]))
                else:
                    messages.error(request, 'Magazine pocket ' + str(form.cleaned_data['tool_number']) + ' is already full')
            else:
                adjust_form = form.save(commit=False)
                machine_tool.delete()
                adjust_form.machine = machine
                adjust_form.tools = machine_tool.tools
                adjust_form.save()
                return HttpResponseRedirect(reverse('machine_tool_list', args=[machine_id]))


    context = {'form': form, 'machine': machine, 'machine_tool': machine_tool}
    return render(request, 'toolroom_app/edit/edit_tool_from_machine_tool_list.html', context)
