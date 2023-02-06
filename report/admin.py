from django.contrib import admin
from .models import Logbook_report
# Register your models here.


@admin.register(Logbook_report)
class Logbook_reportAdmin(admin.ModelAdmin):
    search_fields = ('unit', )
    actions = ['approve_report']
    list_display = ('unit', 'time_of_fault', 'report_read', 'report_approved', 'work_order_created')

    def approve_report(self, request, queryset):
        queryset.update(report_approved=True)