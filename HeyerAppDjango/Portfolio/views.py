from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required

from . import models
from . import serializers
from . import forms


def home(request):
    return render(request, "Portfolio/index.html")
    
def terminal(request):
    return render(request, "Portfolio/terminal.html")

@login_required
def auth_logout(request):
    logout(request)
    return redirect(reverse_lazy("home"))
    
def auth_create(request):
    if request.method == 'POST':
        form = forms.UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = forms.UserCreateForm()
    return render(request, 'Portfolio/signup.html', {'form': form})










#API

class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly,]
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer

class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly,]
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer

class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly,]
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly,]
    queryset = models.Certification.objects.all()
    serializer_class = serializers.CertificationSerializer

class PortfolioViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly,]
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer