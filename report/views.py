from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Logbook_report
from django.contrib import messages
from .forms import ReportForm


# render reports
def reports_list(request):
    """ A View to return all approved/open reports """
    reports = Logbook_report.objects.filter(report_approved=True)
    context = {
        'reports': reports
    }

    return render(request, 'open_reports.html', context)


def report_detail(request, logbook_report_id):
    """ A view to return the report details page """
    report = get_object_or_404(Logbook_report, pk=logbook_report_id)
    context = {
        'report': report,
    }

    return render(request, 'report_detail.html', context)


# render add report page
def add_report(request):
    form = ReportForm(request.POST)

    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            # form.instance.customer_email = request.user.email
            # form.instance.name = request.user.username
            report = form.save(commit=False)
            report.save()        
            messages.success(request, 'Thank you for your Log Book entry, \
            if you provided an email, \
            DSM in Drogheda will email you when your issue has been dealt with.')
        else:
            form = ReportForm()

        return redirect('open_reports.html')  # directed here after adding report
    form = ReportForm()
    context = {
        'form': form, 'report_added': True,
    }
    return render(request, 'add_report.html', context)

