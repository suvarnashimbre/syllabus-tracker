from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from syllabus_tracker.common.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _
from accounts.managers import UserManager
from django.conf import settings
from accounts.constants import UserRole, TeacherRole
# from courses.models import *
from departments.models import *

class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):

    email = models.EmailField(
        _("email address"), unique=True, blank=False, null=False, max_length=254
    )

    first_name = models.CharField(_("First Name"), max_length=254, blank=True)
    last_name = models.CharField(_("Last Name"), max_length=254, blank=True)
    role = models.CharField(max_length=30,choices=UserRole.choices,default=UserRole.STUDENT)
    is_active = models.BooleanField(
        _("active"), default=False, help_text=_("Active user")
    )
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True) 
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("whether the user can log into this admin site."),
    )
    
    USERNAME_FIELD = "email"

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.id}-{self.email}"

    objects = UserManager()

    class Meta:
        verbose_name_plural = "users"
        ordering = ["-created_at", "email"]
        indexes = [models.Index(fields=["email"])]



class Teacher(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE) 
    designation = models.CharField(max_length=50, choices=TeacherRole.choices) 
    joining_date= models.DateField()  
    
    def __str__(self):
        return f"{self.id}-{self.department}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    department = models.ForeignKey('departments.Department', on_delete=models.CASCADE)
    course = models.ForeignKey(
        'courses.Course', on_delete=models.CASCADE, related_name="students"
    ) 
    roll_number = models.CharField(max_length=20, unique=True)
    enrollment_number =  models.CharField(max_length=30, unique=True)
    enrollment_year = models.CharField(_("Admission Year"), max_length=50)
    passing_year = models.CharField(_("Passing Year"), max_length=50)
    current_semester = models.ForeignKey(
        'courses.Semester', on_delete=models.SET_NULL, null=True, related_name="students"
    )
    def __str__(self):
        return f"{self.id}-{self.roll_number}"
    def update_semester(self, semester: 'Semester', year: int):
        """
        Update the current semester of the student and maintain history.
        """
        # Update history for the student
        'StudentSemesterHistory'.objects.create(
            student=self,
            semester=semester,
            year=year,
            is_current=True
        )
        # Mark the previous semester as not current
        self.semester_history.filter(is_current=True).update(is_current=False)
        
        # Update the current semester field
        self.current_semester = semester
        self.save()
