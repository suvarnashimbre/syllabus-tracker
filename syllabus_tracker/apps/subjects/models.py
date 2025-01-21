from django.db import models
from django.utils.translation import gettext_lazy as _
from syllabus_tracker.common.models import TimeStampedModel

class Subject(TimeStampedModel):
    code = models.CharField(max_length=20, unique=True)  # e.g., "CS101"
    name = models.CharField(max_length=100)  # e.g., "Introduction to Programming"
    semester = models.ForeignKey('courses.Semester', on_delete=models.CASCADE, related_name="subjects")
    is_active = models.BooleanField(
        default=True,
        help_text="Whether the subject is currently active or not."
        )

    def __str__(self):
        return f"{self.name} ({self.code}) - {self.semester}"
    
    
    
