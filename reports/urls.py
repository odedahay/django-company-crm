from django.urls import path
from .views import report_view, delete_view, ReportUpdateView


app_name = 'reports'

urlpatterns = [
    path('<str:production_line>/', report_view, name='report-view'),
    path('delete/<pk>/', delete_view, name='delete_view'),
    path('<str:production_line>/<pk>/update/', ReportUpdateView.as_view(), name='update-view'),
]

# update
#/{{obj.production_line}}/obj.pk/update/