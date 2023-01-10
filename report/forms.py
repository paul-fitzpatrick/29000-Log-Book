from .models import Logbook_report
from django import forms


class ReportForm(forms.ModelForm):
    class Meta:
        model = Logbook_report
        fields = ('Grade',
                  'driver_name',
                  'driver_email',
                  'unit',
                  'location_at_time_of_fault',
                  'details_of_defect')
