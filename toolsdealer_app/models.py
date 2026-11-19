from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

#Tools info Dictionaries
tool_material_capability_choice = (
    ('carbide', 'CARBIDE'),
    ('hss', 'HSS'),
    ('cast alloys', 'CAST ALLOYS'),
    ('tungsten carbide', 'TUNGSTEN CARBIDE'),
    ('oxides', 'OXIDES'),
    ('diamonds', 'DIAMONDS'),
)

tool_operation_choice = (
    ('holder', 'holder'),
    ('collet', 'collet'),
    ('mill', 'milling'),
    ('drill', 'drilling'),
    ('bore', 'boring'),
    ('tap', 'tapping'),
    ('saw', 'saw'),
    ('turn', 'turning'),
    )

taper_angle_choice = (
    ('10', '10'),
    ('20', '20'),
    ('30', '30'),
    ('45', '45'),
    ('55', '55'),
    ('60', '60'),
    )

tool_tool_diameter_choice = (
    ('11x80','11x80'),
    ('11x100','11x100'),
    ('11x120','11x120'),
    ('16x80','16x80'),
    ('16x100','16x100'),
    ('16x120','16x120'),
    ('32x80','32x80'),
    ('32x100','32x100'),
    ('32x120','32x120'),
    ('40x80','40x80'),
    ('40x100','40x100'),
    ('40x120','40x120'),
)

boring_tool_diameter_range = (
    ('1-5', '1-5'),
    ('5-8', '5-8'),
    ('8-11', '8-11'),
    ('11-14', '11-14'),
    ('14-17', '14-17'),
    ('17-20', '17-20'),
    )

holder_choice = (
    ('standard holder', 'standard holder'),
    ('precision holder', 'precision holder'),
    ('heat shrink holder', 'heat shrink holder'),
    )

collet_choice = (
    ('standard collet', 'standard collet'),
    ('precision collet', 'precision collet'),
    )


# MILLING OPERATION TOOLS.
class FaceMill(models.Model):
    """Defining Information for Facemill."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='face mill', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(999)])
    corner_radius = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(999)])
    taper_angle = models.CharField(max_length=50, choices=taper_angle_choice)
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_shoulder_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_insert_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    start_sholder_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    body_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

class EndMill(models.Model):
    """Defining Information for Endmill."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='end mill', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

class BullMill(models.Model):
    """Defining Information for BullMill."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='bull mill', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tool_corner_radius = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

class BallMill(models.Model):
    """Defining Information for BallMill."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='ball mill', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

class Tcutter(models.Model):
    """Defining Information for T-Cutter."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='t-cutter', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    corner_radius = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

class DoveTail(models.Model):
    """Defining Information for DoveTail."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='dovetail', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    corner_radius = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    taper_angle = models.CharField(max_length=50, choices=taper_angle_choice)
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")
    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø - "

class Lollipop(models.Model):
    """Defining Information for Lollipop."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='lollipop', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")
    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "mmØ"

class Engraver(models.Model):
    """Defining Information for Engraver."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='engraver', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tip_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    corner_radius = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    taper_angle = models.CharField(max_length=50, choices=taper_angle_choice)
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø - "

class ThreadMill(models.Model):
    """Defining Information for ThreadMill."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='thread mill', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_teeth = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/drillingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

# DRILLING OPERATION TOOLS.
class Drill(models.Model):
    """Defining Information for Drills."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='drill', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tip_angle = models.PositiveIntegerField(default=118, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/drillingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

class SpotDrill(models.Model):
    """Defining Information for Spot Drills."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='spot drill', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tip_angle = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/drillingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

class CenterDrill(models.Model):
    """Defining Information for Center Drill."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='center drill', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tip_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tip_angle = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_angle = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/drillingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

class BoringBar(models.Model):
    """Defining Information for BoringBar."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='boring bar', editable=False)
    tool_diameter = models.CharField(max_length=50, choices= boring_tool_diameter_range)
    corner_radius = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/drillingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - Diameter Range: " + (self.tool_diameter)

class Tap(models.Model):
    """Defining Information for Tap."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='thread tap', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    pitch = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tip_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    arbor_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    chamfer_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    cutting_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    total_length = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/drillingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

# PARTING OPERATION TOOLS.
class Saw(models.Model):
    """Defining Information for Saw Blade."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='saw blade', editable=False)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    tool_internal_diameter = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    shank_width = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    saw_thickness = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    blade_thickness = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    number_of_flutes = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " - " + self.tool_material_capability + " - " + str(self.tool_diameter) + "Ø"

# TURNING OPERATION TOOLS.
class ExternalTurningTool(models.Model):
    """Defining Information for external turning tool."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='external turning', editable=False)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/turningtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type

class InternalTurningTool(models.Model):
    """Defining information internal Turning tool."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='internal turning', editable=False)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/turningtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type

class PartingTool(models.Model):
    """Defining Information for Parting off Tool."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='parting tool', editable=False)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/turningtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type

class ThreadingTool(models.Model):
    """Defining Information for Threading tool."""

    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, null=False, default='threading tool', editable=False)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/turningtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type

#TOOL HOLDER AND COLLET
class Holder(models.Model):
    """"Defining Information for tool Standard holder"""
    diameter_choice =(
        ('ER11','0.5-7.0'),
        ('ER16','0.5-9.0'),
        ('ER20','1.0-13.0'),
        ('ER25','1.0-16.0'),
        ('ER32','1.0-21.0'),
        ('ER40','3.0-26.0'),
    )
    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, choices=holder_choice)
    tool_diameter = models.CharField(max_length=50, choices=diameter_choice)

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " " + self.tool_diameter

class Collet(models.Model):
    """"Defining Information for tool Heat Standard Collet"""
    diameter_choice =(
            ('ER11','0.5-7.0'),
            ('ER16','0.5-9.0'),
            ('ER20','1.0-13.0'),
            ('ER25','1.0-16.0'),
            ('ER32','1.0-21.0'),
            ('ER40','3.0-26.0'),
        )
    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    tool_type = models.CharField(max_length=50, choices=collet_choice)
    tool_diameter = models.CharField(max_length=50, choices=diameter_choice)

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.tool_type + " " + self.tool_diameter + "mm"
