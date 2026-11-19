from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class ToolsStock(models.Model):
    """Insert Tool into Production database."""
    material_choice = (
    ('carbide', 'CARBIDE'),
    ('hss', 'HSS'),
    )

    tool_type_choice = (
    ('facemill', 'Facemill'),
    ('endmill', 'Endmill'),
    ('bullmill', 'Bullmill'),
    ('ballmill', 'Ballmill'),
    ('chamfer tool', 'Chamfer Tool'),
    ('spotdrill', 'Spotdrill'),
    ('drill', 'Drill'),
    ('tcutter', 'Tcutter'),
    )

    tool_material = models.CharField(max_length=15, choices=material_choice)
    tool_type = models.CharField(max_length=200, choices=tool_type_choice)
    tool_diameter = models.CharField(max_length=200)
    tool_cut_length = models.CharField(max_length=200)
    tool_total_length = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(300)])
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.tool_type + " - " + self.tool_diameter + "Ø"

class MachinesSector(models.Model):
    """Display Floor Machine Cells/Sector."""
    sector_choice = (
    ('Milling', 'MILLING'),
    ('Turning', 'TURNING'),
    )

    sector = models.CharField(max_length=15, choices=sector_choice)

    def __str__(self):
        return self.sector

class MachinesCell(models.Model):
    """Register Cell into machines sector."""
    machines_sector = models.ForeignKey(MachinesSector, on_delete=models.CASCADE, related_name='registercell_set')
    cell_name = models.TextField(max_length=30)

    def __str__(self):
        """Return a String representation of the model."""
        return self.cell_name

class Machines(models.Model):
    """Register Machines into Cells."""

    machines_cell = models.ForeignKey(MachinesCell, null=True, on_delete=models.CASCADE, related_name='registermachines_set')
    machine_name = models.TextField(max_length=30)
    machine_axis_amount = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    machine_z_size = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(500)])
    machine_x_size = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(350)])
    machine_y_size = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(300)])
    machine_magazine_qty = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1), MaxValueValidator(999)])

    def __str__(self):
        """Return a String representation of de Machine Name."""
        return self.machine_name

class MachineToolList(models.Model):
    """Register Tool List of each Machine."""
    machine = models.ForeignKey(Machines, null=False, on_delete=models.CASCADE)
    tools = models.ForeignKey(ToolsStock, null=False, on_delete=models.CASCADE)
    tool_number = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tool_height = models.DecimalField(max_digits=10, decimal_places=3, default=0, validators=[MinValueValidator(-999), MaxValueValidator(999)])
    tool_height_wear = models.DecimalField(max_digits=10, decimal_places=3, default=0, validators=[MinValueValidator(-999), MaxValueValidator(999)])
    tool_radius = models.DecimalField(max_digits=10, decimal_places=3, default=0, validators=[MinValueValidator(-999), MaxValueValidator(999)])
    tool_radius_wear = models.DecimalField(max_digits=10, decimal_places=3, default=0, validators=[MinValueValidator(-999), MaxValueValidator(999)])
    outside_holder_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'tools list'
