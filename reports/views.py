from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReportForm, ProblemReportedForm
from .models import Report
from areas.models import ProductionLine
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView


class ReportUpdateView(UpdateView):
    model = Report
    form_class = ReportForm
    template_name = 'reports/update.html'

    def get_success_url(self):
        return self.request.path

@login_required
def delete_view(request, *args, **kwargs):
    r_id =  kwargs.get('pk')
    obj = Report.objects.get(id=r_id)
    obj.delete()

    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def report_view(request, production_line):
    form = ReportForm(request.POST or None, production_line=production_line)
    pform = ProblemReportedForm(request.POST or None)
    queryset = Report.objects.filter(production_line__name=production_line)
    line = get_object_or_404(ProductionLine, name=production_line)

    if 'submitbtn1' in request.POST:
        r_id = request.POST.get('report_id')

        if pform.is_valid():
            report = Report.objects.get(id=r_id)

            obj = pform.save(commit=False)
            obj.user = request.user
            obj.report = report
            obj.save()

            # reset the forms
            # form = ReportForm()
            # pform = ProblemReportedForm()

            return redirect(request.META.get('HTTP_REFERER'))

    elif 'submitbtn2' in request.POST:
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.production_line = line
            obj.save()

            # reset the forms
            # form = ReportForm()
            # pform = ProblemReportedForm()
            return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'form' : form,
        'pform' : pform,
        'object_list': queryset,
    }

    return render(request, 'reports/report.html', context)


