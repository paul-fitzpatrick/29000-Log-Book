from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Logbook_report
from django.contrib import messages
from .forms import ReportForm


# render add review page
def add_report(request):
    form = ReportForm(request.POST)

    if request.method == "POST":
        form = ReporForm(request.POST)
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

        return redirect('add_report.html')  # directed here after adding report
    form = ReportForm()
    context = {
        'form': form, 'add_report': True,
    }
    return render(request, 'add_report.html', context)


