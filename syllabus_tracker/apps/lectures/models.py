from django.db import models
from django.utils.translation import gettext_lazy as _
from syllabus_tracker.common.models import TimeStampedModel
    
class Lecture(TimeStampedModel):
    syllabus_unit = models.ForeignKey('syllabus.SyllabusUnit', on_delete=models.CASCADE, related_name='lectures')
    lecture_code = models.CharField(max_length=20, unique=True, help_text="Unique code for the lecture")
    title = models.CharField(max_length=255, help_text="Title of the lecture")
    date = models.DateField(help_text="Date of the lecture")
    start_time = models.TimeField(help_text="Start time of the lecture")
    end_time = models.TimeField(help_text="End time of the lecture")
    location = models.CharField(max_length=255, help_text="Location or classroom for the lecture")
    instructor = models.ForeignKey('accounts.Teacher', on_delete=models.CASCADE, related_name='lectures', null=True)
    is_active = models.BooleanField(default=True, help_text="Indicates if the lecture is active or canceled")

    def __str__(self):
        return f"Lecture {self.lecture_code} - {self.title} ({self.date})"

    class Meta:
        verbose_name_plural = "Lectures"
        
        
class Attendance(TimeStampedModel):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE, related_name='attendances')
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='attendances')
    is_present = models.BooleanField(default=False, help_text="Indicates whether the student was present or absent.")
    attendance_date = models.DateField(auto_now_add=True, help_text="The date the attendance was recorded")

    def __str__(self):
        return f"Attendance for {self.student} in {self.lecture.title}"

    class Meta:
        unique_together = ('lecture', 'student')  # En