from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import DjangoModelPermissions


from . import models
from . import serializers


def home(request):
    return render(request, "Portfolio/index.html")
    
def terminal(request):
    return render(request, "Portfolio/terminal.html")

class SkillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer

class ExperienceViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer

class EducationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer

class CertificationViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Certification.objects.all()
    serializer_class = serializers.CertificationSerializer

class PortfolioViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer