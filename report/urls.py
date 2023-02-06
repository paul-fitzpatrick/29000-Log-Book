from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from report.views import reports_list


urlpatterns = [
    path('open_reports.html', views.reports_list, name='reports_list'),
    path('report_detail.html/<logbook_report_id>/', views.report_detail, name='report_detail'),
    path('add_report.html', views.add_report, name='add_report'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)