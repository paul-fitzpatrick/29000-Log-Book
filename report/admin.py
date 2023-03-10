from django.contrib import admin
from .models import Logbook_report
# Register your models here.


@admin.register(Logbook_report)
class Logbook_reportAdmin(admin.ModelAdmin):
    search_fields = ('unit',)
    actions = ['report_read',]
    list_display = ('unit', 'time_of_fault', 'report_read', 'work_order_created', 'work_order_closed', 'driver_responded_to')

    def approve_report(self, request, queryset):
        queryset.update(report_approved=True)