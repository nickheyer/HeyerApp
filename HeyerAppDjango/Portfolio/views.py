from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import RedirectView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as UserModel
from django.contrib.auth.decorators import login_required


from . import mixins
from . import models
from . import serializers
from . import forms

from datetime import timedelta
from django.utils import timezone


class Home(TemplateView):
    template_name = "Portfolio/index.html"
    model = models.FeedEvent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        startdate = timezone.now()
        enddate = startdate - timedelta(days=120)
        context['events'] = models.FeedEvent.objects.filter(eventdate__gte=enddate)
        
        return context


class Skills(ListView):
    model = models.Skill
    template_name = "Portfolio/skills.html"

class SkillCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Skill
    form_class = forms.SkillForm
    template_name = "Portfolio/skill_create_form.html"

class SkillDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Skill
    template_name = "Portfolio/skill_delete_form.html"
    success_url = "/skills"

class SkillUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Skill
    form_class = forms.SkillForm
    template_name = "Portfolio/skill_update_form.html"
    success_url = "/skills"



class Experience(ListView):
    model = models.Experience
    template_name = "Portfolio/experience.html"

class ExperienceCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Experience
    form_class = forms.ExperienceForm
    template_name = "Portfolio/experience_create_form.html"

class ExperienceDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Experience
    template_name = "Portfolio/experience_delete_form.html"
    success_url = "/experience"

class ExperienceUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Experience
    form_class = forms.ExperienceForm
    template_name = "Portfolio/experience_update_form.html"
    success_url = "/experience"



class Education(ListView):
    model = models.Education
    template_name = "Portfolio/education.html"

class EducationCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Education
    form_class = forms.EducationForm
    template_name = "Portfolio/education_create_form.html"

class EducationDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Education
    template_name = "Portfolio/education_delete_form.html"
    success_url = "/education"

class EducationUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Education
    form_class = forms.EducationForm
    template_name = "Portfolio/education_update_form.html"
    success_url = "/education"



class Certifications(ListView):
    model = models.Certification
    template_name = "Portfolio/certifications.html"

class CertificationCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Certification
    form_class = forms.CertificationForm
    template_name = "Portfolio/certification_create_form.html"

class CertificationDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Certification
    template_name = "Portfolio/certification_delete_form.html"
    success_url = "/certifications"

class CertificationUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Certification
    form_class = forms.CertificationForm
    template_name = "Portfolio/certification_update_form.html"
    success_url = "/certifications"



class Projects(ListView):
    model = models.Project
    template_name = "Portfolio/projects.html"

class ProjectCreate(mixins.AdminRequiredMixin, CreateView):
    model = models.Project
    form_class = forms.ProjectForm
    template_name = "Portfolio/project_create_form.html"

class ProjectDelete(mixins.AdminRequiredMixin, DeleteView):
    model = models.Project
    template_name = "Portfolio/project_delete_form.html"
    success_url = "/portfolio"

class ProjectUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectForm
    template_name = "Portfolio/project_update_form.html"
    success_url = "/projects"








class Terminal(TemplateView):
    template_name = "Portfolio/terminal.html"


@login_required
def auth_logout(request):
    logout(request)
    return redirect(reverse_lazy("home"))


class UserCreate(CreateView):
    model = UserModel
    form_class = forms.UserCreateForm
    template_name = 'Portfolio/signup.html'
    def get_success_url(self):
        return reverse_lazy('login')

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

class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, permissions.DjangoModelPermissionsOrAnonReadOnly,]
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer