from .models import Logbook_report
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class ReportForm(forms.ModelForm):
    class Meta:
        model = Logbook_report
        fields = ('Grade',
                  'driver_name',
                  'driver_email',
                  'unit',
                  'location_at_time_of_fault',
                  'time_of_fault',
                  'date_of_fault',
                  'details_of_defect')
        
        widgets = {
            'date_of_fault': DateInput(),
            'time_of_fault': forms.TimeInput(attrs={'type': 'time'})
        }

    # def __init__(self, *args, **kwargs):
    #     """
    #     Add placeholders and classes, remove auto-generated
    #     labels and set autofocus on first field
    #     """
    #     super().__init__(*args, **kwargs)
    #     placeholders = {
    #         'Grade': 'Grade',
    #         'driver_name': 'driver_name',
    #         'driver_email': 'driver_email (optional)',
    #         'unit': 'unit',
    #         'location_at_time_of_fault': 'location_at_time_of_fault',
    #         'time_of_fault': 'time_of_fault',
    #         'date_of_fault': 'date_of_fault',
    #         'details_of_defect': 'details_of_defect'

    #     }
    #     self.fields['Grade'].widget.attrs['autofocus'] = True
    #     for field in self.fields:
    #         if self.fields[field].required:
    #             placeholder = f'{placeholders[field]} *'
    #         else:
    #             placeholder = placeholders[field]
    #         self.fields[field].widget.attrs['placeholder'] = placeholder
    #         self.fields[field].widget.attrs['class'] = 'form-input'
    #         self.fields[field].label = False



