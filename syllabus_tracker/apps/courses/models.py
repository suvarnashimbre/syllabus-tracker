from django.db import models
from django.utils.translation import gettext_lazy as _
from departments.constants import DEGREE_CHOICES
from syllabus_tracker.common.models import TimeStampedModel
from departments.models import Department
from accounts.models import Student
    

class Course(TimeStampedModel):
    name = models.CharField(max_length=100)  
    code = models.CharField(choices=DEGREE_CHOICES,max_length=20, unique=True ) 
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="courses"
    ) 
    duration_years = models.PositiveIntegerField()  
    description = models.TextField(blank=True, null=True)  
    is_active = models.BooleanField(
        default=True,
        help_text=_("Whether this course is active or not.")
        )
    def __str__(self):
        return f"{self.name} ({self.department.code})"
    
    

class Semester(TimeStampedModel):
    number = models.IntegerField()  # e.g., 1, 2, 3, etc.
    degree = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="semesters")
    is_active = models.BooleanField(
        default=True,
        help_text=_("Whether this semester is active or not.")
        )

    def __str__(self):
        return f"Semester {self.number} - {self.degree.name}"

class StudentSemesterHistory(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="semester_history")
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name="semester_history")
    year = models.PositiveIntegerField(help_text="The academic year (e.g., 2024)")
    date_changed = models.DateTimeField(auto_now_add=True)
    is_current = models.BooleanField(default=True, help_text="Indicates if this is the current semester for the student")

    def __str__(self):
        return f"{self.student} - {self.semester} - {self.year}"

    class Meta:
        verbose_name_plural = "Student Semester Histories"
        ordering = ['-date_changed']



