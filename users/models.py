from django.db import models
from django.contrib.auth.models import User

class Member(models.Model):
    province_choices = [
        ("1", "Province No. 1"), 
        ("2", "Province No. 2"), 
        ("3", "Bagmati Pradesh"), 
        ("4", "Gandaki Pradesh"), 
        ("5", "Province No. 5"),
        ("6", "Karnali Pradesh"),
        ("7", "Sudurpashchim Pradesh"),
    ]

    username        = models.CharField(max_length=255)
    mobile_number   = models.IntegerField()
    province        = models.CharField(max_length=20, choices=province_choices)
    district        = models.CharField(max_length=20)
    campus          = models.CharField(max_length=200)
    current_role    = models.CharField(max_length=50)
    municipality    = models.CharField(max_length=100)
    ward            = models.IntegerField()
    added_by        = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)

    def __str__(self):
        return self.username

    def has_add_permission(self, request):
        return False