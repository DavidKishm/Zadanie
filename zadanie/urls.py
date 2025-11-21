from django.contrib import admin
from django.urls import path
from service.views import (
    home, CreateIncidentView, ListIncidentsView, UpdateIncidentStatusView
)

urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/incidents/', ListIncidentsView.as_view()),
    path('api/incidents/create/', CreateIncidentView.as_view()),
    path('api/incidents/<int:id>/status/', UpdateIncidentStatusView.as_view()),
]
