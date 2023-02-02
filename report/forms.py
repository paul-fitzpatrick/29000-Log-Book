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
                  'time_of_fault',
                  'details_of_defect')
        
        widgets = {
            
            'time_of_fault': forms.TimeInput(attrs={'type': 'time'})
        }
