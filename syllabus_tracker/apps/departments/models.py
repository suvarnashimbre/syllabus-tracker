from django.db import models
from django.utils.translation import gettext_lazy as _
from departments.constants import DepartmentCode, DEGREE_CHOICES
from syllabus_tracker.common.models import TimeStampedModel
# from accounts.models import Teacher

class Department(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)  
    code = models.CharField(
        max_length=20,
        choices=DepartmentCode.choices,
        unique=True
    )
    # head_of_department = models.OneToOneField(Teacher, on_delete=models.SET_NULL, null=True, blank=True) 
    established_date = models.DateField()  
    description = models.TextField(blank=True, null=True)  
    is_active = models.BooleanField(
        default=True,
        help_text=_("Whether this department is active or not.")
        )
    def __str__(self):
        return self.name
    
    
