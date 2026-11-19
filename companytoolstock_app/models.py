from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
from toolsdealer_app.models import *
from toolroom_app.models import *
'''
    CTSDB stands for = COMPANY TOOL STOCK DATABASE
'''
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
tool_type_choice = (
    ('Facemill', 'facemill'),
    ('Endmill', 'endmill'),
    ('Ballmill', 'ballmill'),
    ('Bullmill', 'bullmill'),
    ('Tcutter', 'tcutter'),
    ('Dovetail', 'dovetail'),
    ('Lollipop', 'lollipop'),
    ('Engraver', 'engraver'),
    ('Threadmill', 'threadmill'),
    ('drill', 'drill'),
    ('spotdrill', 'spotdrill'),
    ('tap', 'tap'),
    )
tool_material_capability_choice = (
    ('carbide', 'CARBIDE'),
    ('hss', 'HSS'),
    ('cast alloys', 'CAST ALLOYS'),
    ('tungsten carbide', 'TUNGSTEN CARBIDE'),
    ('oxides', 'OXIDES'),
    ('diamonds', 'DIAMONDS'),
)
angle_choice = (
    ('10', '10'),
    ('20', '20'),
    ('30', '30'),
    ('45', '45'),
    ('55', '55'),
    ('60', '60'),
    )
insert_type_choice = (
    ('C', 'C'),
    ('D', 'D'),
    ('K', 'K'),
    ('R', 'R'),
    ('S', 'S'),
    ('T', 'T'),
    ('V', 'V'),
    ('W', 'W'),
    )
thread_size_mm = (
    ('M3','M3'),
    ('M4','M4'),
    ('M5','M5'),
    ('M6','M6'),
    ('M8','M8'),
    ('M10','M10'),
    ('M12','M12'),
    ('M14','M14'),
    ('M16','M16'),
    ('M18','M16'),
    ('M20','M20'),
    ('M22','M22'),
    ('M24','M24'),
)
pitch_size_mm = (
    ('0.5','0.5'),
    ('0.7','0.7'),
    ('0.8','0.8'),
    ('1.0','1.0'),
    ('1.25','1.25'),
    ('1.50','1.50'),
    ('1.75','1.25'),
    ('2.0','2.0'),
    ('2.5','2.5'),
    ('3.0','3.0'),
    ('4.0','4.0'),
    ('4.5','4.5'),
    ('5.0','5.0'),
)
thread_size_in = (
    ('1-8','1-8'),
    ('1(1/8)-8','1(1/8)-8'),
    ('1(1/4)-8','1(1/4)-8'),
    ('1(3/8)-8','1(3/8)-8'),
    ('1(1/2)-8','1(1/2)-8'),
    ('1(5/8)-8','1(5/8)-8'),
    ('1(3/4)-8','1(3/4)-8'),
    ('1(7/8)-8','1(7/8)-8'),
    ('2-8','2-8'),
    ('2(1/4)-8','2(1/4)-8'),
)
pitch_size_in = (
    ('0.5','0.5'),
    ('0.7','0.7'),
    ('0.8','0.8'),
    ('1.0','1.0'),
    ('1.25','1.25'),
    ('1.50','1.50'),
    ('1.75','1.25'),
    ('2.0','2.0'),
    ('2.5','2.5'),
    ('3.0','3.0'),
    ('4.0','4.0'),
    ('4.5','4.5'),
    ('5.0','5.0'),
)

holder_choice = (
    ('standard holder', 'standard holder'),
    ('precision holder', 'precision holder'),
    ('heat shrink holder', 'heat shrink holder'),
    ('side lock', 'side lock'),
    ('Haimer', 'Haimer'),
    )
holder_bt_choice =(
    ('BT30','BT30'),
    ('BT40','BT40'),
    ('BT50','BT50'),
    )
holder_er_choice =(
    ('ER8','ER8'),
    ('ER11','ER11'),
    ('ER16','ER16'),
    ('ER20','ER20'),
    ('ER25','ER25'),
    ('ER32','ER32'),
    ('ER40','ER40'),
    ('ER50','ER50'),
    )
holder_diameter_choice =(
    ('0.1-0.9','0.1 - 0.9'),
    ('0.9-1.9','0.9 - 1.9'),
    ('1.9-2.9','1.9 - 2.9'),
    ('2.9-4.9','2.9 - 4.9'),
    ('4.9-6.9','4.9 - 6.9'),
    ('6.9-8.9','6.9 - 8.9'),
    ('8.9-10.9','8.9 - 10.9'),
    ('10.9-13.9','10.9 - 13.9'),
    ('13.9-16.9','13.9 - 16.9'),
    ('16.9-20.9','16.9 - 20.9'),
    ('20.9-25.9','20.9 - 25.9'),
    ('25.9-30.9','25.9 - 30.9'),
    ('30.9-35.9','30.9 - 35.9'),
    ('35.9-40.9','35.9 - 40.9'),
    ('45.9-50.9','45.9 - 50.9'),
    ('50.9-60.9','50.9 - 60.9'),
    ('60.9-70.9','60.9 - 70.9'),
    )
holder_length_choice =(
    ('60','60'),
    ('70','70'),
    ('80','80'),
    ('90','90'),
    ('100','100'),
    ('130','130'),
    ('160','160'),
    )

collet_choice = (
    ('standard collet', 'standard collet'),
    ('precision collet', 'precision collet'),
    )

class Holder(models.Model):
    """Holder"""

    operation = models.CharField(max_length=50, editable=False, default=tool_operation_choice[0], choices=tool_operation_choice)
    type = models.CharField(max_length=50, null=False, choices=holder_choice)
    bt = models.CharField(max_length=50, null=False, choices=holder_bt_choice)
    er = models.CharField(max_length=50, null=True, blank=True, choices=holder_er_choice)
    a = models.CharField(max_length=50, null=False, choices=holder_length_choice)
    clamp_range = models.CharField(max_length=50, null=False, choices=holder_diameter_choice)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(9999)])

    def __str__(self):
        """Return a string representation of the Operation."""
        return str(self.type)

class Collet(models.Model):
    """Collet"""
    operation = models.CharField(max_length=50, choices=tool_operation_choice)
    type = models.CharField(max_length=50, choices=collet_choice)
    clamp_range = models.CharField(max_length=50, choices=holder_diameter_choice)
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(9999)])
    def __str__(self):
        """Return a string representation of the Operation."""
        return str(self.type)

class Tool(models.Model):
    """Tools"""

    operation = models.CharField(max_length=50, null=False, choices=tool_operation_choice)
    type = models.CharField(max_length=50, null=False, choices=tool_type_choice)
    tool_material_capability = models.CharField(max_length=50, choices=tool_material_capability_choice)
    tool_diameter = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    corner_radius = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    corner_angle = models.CharField(max_length=50, blank=True, null=True, choices=angle_choice)
    shank_diameter = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    shank_length = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    arbor_diameter = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    cutting_length = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    number_of_flutes = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)])
    insert_type = models.CharField(max_length=50, blank=True, null=True, choices=insert_type_choice)
    insert_length = models.PositiveIntegerField(default=0, blank=True, validators=[MinValueValidator(0), MaxValueValidator(999)])
    insert_angle = models.CharField(max_length=50, blank=True, null=True, choices=angle_choice)
    tool_total_length = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(0), MaxValueValidator(9999)])
    image = models.ImageField(null=True, blank=True, upload_to="toolsdealer_images/millingtools")

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.type

class ToolSetUp(models.Model):
    """First Form for Tool Setup."""
    sector = models.ForeignKey(MachinesSector, null=False, on_delete=models.CASCADE)
    cell = models.ForeignKey(MachinesCell, null=False, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machines, null=False, on_delete=models.CASCADE)
    holder_type = models.ForeignKey(Holder, null=False, on_delete=models.CASCADE, related_name='setup_holder')
    holder_specs = models.ForeignKey(Holder, null=False, on_delete=models.CASCADE, related_name='setup_holder_specs')
    collet_type = models.ForeignKey(Collet, null=True, blank=True, on_delete=models.CASCADE, related_name='setup_collet')
    collet_specs = models.ForeignKey(Collet, null=True, blank=True, on_delete=models.CASCADE, related_name='setup_collet_specs')
    tool_type = models.ForeignKey(Tool, null=False, on_delete=models.CASCADE, related_name='setup_tool_type')
    tool_specs = models.ForeignKey(Tool, null=False, on_delete=models.CASCADE, related_name='setup_tool_specs')
    tool_diameter = models.ForeignKey(Tool, null=False, on_delete=models.CASCADE, related_name='setup_tool_diameter')
    tool_shoulder_length = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])
    tool_ohl = models.FloatField(null=False, validators=[MinValueValidator(0.0), MaxValueValidator(500.0)])

    def __str__(self):
        """Return a string representation of the Operation."""
        return self.sector.sector + " - " + self.cell.cell_name + " - " + self.machine.machine_name + self.tool_type
