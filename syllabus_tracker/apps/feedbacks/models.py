from django.db import models
from django.utils.translation import gettext_lazy as _
from syllabus_tracker.common.models import TimeStampedModel
from django.core.exceptions import ValidationError

class LectureFeedback(TimeStampedModel):
    lecture = models.ForeignKey('lectures.Lecture', on_delete=models.CASCADE, related_name='feedbacks')
    student = models.ForeignKey('accounts.Student', on_delete=models.CASCADE, related_name='feedbacks')
    rating = models.PositiveIntegerField(choices=[(1, 'Poor'), (2, 'Fair'), (3, 'Good'), (4, 'Very Good'), (5, 'Excellent')])
    comments = models.TextField(blank=True, null=True, help_text="Optional comments by the student")
    feedback_date = models.DateField(auto_now_add=True, help_text="The date the feedback was given")

    def clean(self):
        # Check if the student attended the lecture before allowing feedback submission
        attendance = Attendance.objects.filter(lecture=self.lecture, student=self.student).first()
        if not attendance or not attendance.is_present:
            raise ValidationError("Only students who attended the lecture can give feedback.")

    def save(self, *args, **kwargs):
        # Call the clean method to validate attendance before saving
        self.clean()
        super(LectureFeedback, self).save(*args, **kwargs)

    def __str__(self):
        return f"Feedback from {self.student} on {self.lecture.title}"

    class Meta:
        unique_together = ('lecture', 'student')  # Prevent multiple feedbacks from the same student on the same lecture
