from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# from review.views import reviews_list


urlpatterns = [
    path('add_report.html', views.add_report, name='add_report'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)