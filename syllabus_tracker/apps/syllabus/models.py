from django.db import models
from django.utils.translation import gettext_lazy as _
from syllabus_tracker.common.models import TimeStampedModel

    
class SyllabusUnit(TimeStampedModel):
    subject = models.ForeignKey('subjects.Subject', on_delete=models.CASCADE, related_name='syllabus_units')
    unit_code = models.CharField(max_length=20, unique=True, help_text="Unique code for the syllabus unit")
    title = models.CharField(max_length=255, help_text="Title of the syllabus unit")
    description = models.TextField(blank=True, null=True, help_text="Detailed description/sub-topics of the unit")
    semester = models.ForeignKey('courses.Semester',on_delete=models.CASCADE, help_text="Semester in which the syllabus unit is taught (e.g., 1, 2, etc.)")
    

    def __str__(self):
        return f"{self.subject.name} - {self.title} ({self.unit_code})"
    
    
    
    