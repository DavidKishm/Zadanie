from django.db import models
from rest_framework import serializers, generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render


class Incident(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('in_progress', 'В работе'),
        ('resolved', 'Решен'),
        ('closed', 'Закрыт'),
    ]
    SOURCE_CHOICES = [
        ('operator', 'Оператор'),
        ('monitoring', 'Мониторинг'),
        ('partner', 'Партнер'),
    ]
    description = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new')
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
        read_only_fields = ('id', 'created_at')


def home(request):
    return render(request, "home.html")


class CreateIncidentView(generics.CreateAPIView):
    queryset = Incident.objects.all()
    serializer_class = IncidentSerializer


class ListIncidentsView(generics.ListAPIView):
    serializer_class = IncidentSerializer

    def get_queryset(self):
        qs = Incident.objects.all().order_by("-created_at")
        status_param = self.request.query_params.get("status")
        if status_param:
            qs = qs.filter(status=status_param)
        return qs


class UpdateIncidentStatusView(generics.GenericAPIView):
    serializer_class = IncidentSerializer
    lookup_url_kwarg = "id"

    def patch(self, request, id):
        incident = get_object_or_404(Incident, id=id)
        new_status = request.data.get("status")
        if not new_status:
            return Response({"detail": "Статус отсутствует"}, status=400)
        incident.status = new_status
        incident.save()
        return Response(IncidentSerializer(incident).data)
