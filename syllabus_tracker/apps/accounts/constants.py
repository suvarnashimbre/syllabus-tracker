from django.db.models import TextChoices


class UserRole(TextChoices):
    STUDENT = "STUDENT", "Student"
    TEACHER  = "TEACHER", "Teacher"


class TeacherRole(TextChoices):
    PROFESSOR = "PROFESSOR" "Professor"
    ASSISTANT_PROFESSOR = "ASSISTANT_PROFESSOR", "Assistant Professor"
    LECTURER =  "LECTURER", "Lecturer"
    
