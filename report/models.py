from django.db import models
import datetime
from django.contrib.auth.models import User


class Logbook_report(models.Model):
    Grade = models.CharField(max_length=25, default='Driver')
    driver_name = models.CharField(max_length=50)
    driver_email = models.EmailField(blank=True)  # blank =  make optional
    unit = models.IntegerField(default=29)
    location_at_time_of_fault = models.TextField(max_length=60)
    time_of_fault = models.TimeField(null=True, blank=True)
    date_of_fault = models.TextField()
    details_of_defect = models.TextField()
    # admin
    report_read = models.BooleanField(default=False)
    work_order_created = models.BooleanField(default=False)
    driver_responded_to = models.BooleanField(default=False)
    # report_approved = models.BooleanField(default=False)
    work_order_closed = models.BooleanField(default=False)
    # broken seal info to be added
    
    class Meta:         
        ordering = ['date_of_fault']

    def __str__(self):
        return self.driver_name

    