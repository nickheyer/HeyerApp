from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import RedirectView

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User as UserModel
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver


from . import mixins
from . import models
from . import serializers
from . import forms
from . import decorators

from datetime import timedelta
from django.utils import timezone


class Home(TemplateView):
    template_name = "Portfolio/index.html"
    model = models.FeedEvent

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        startdate = timezone.now()
        enddate = startdate - timedelta(days=6)
        feeds = models.FeedEvent.objects.filter(eventdate__gte=enddate)

        context['events'] = models.FeedEvent.objects.filter(
            eventdate__gte=startdate - timedelta(days=120)).order_by('-id')[:16]
        context['status'] = models.StatusEvent.objects.latest('id')
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
    success_url = "/projects"


class ProjectUpdate(mixins.AdminRequiredMixin, UpdateView):
    model = models.Project
    form_class = forms.ProjectForm
    template_name = "Portfolio/project_update_form.html"
    success_url = "/projects"


class Terminal(TemplateView):
    template_name = "Portfolio/terminal.html"


class UserCreate(CreateView):
    model = UserModel
    form_class = forms.UserCreateForm
    template_name = 'Portfolio/signup.html'


    def get_success_url(self):
        next = self.request.GET.get('next')
        if next:
            return reverse_lazy('Portfolio:login')+f"?next={next}"
        return reverse_lazy('Portfolio:login')


@login_required
def auth_logout(request):
    logout(request)
    next = request.GET.get('next')
    if next:
        return redirect(next)
    return redirect(reverse_lazy("Portfolio:home"))


#Creates feed event when a skill, certificate, etc. model is updated
@decorators.receiver_with_multiple_senders(signal=post_save, senders=[models.Skill, models.Certification, models.Education, models.Experience, models.Project])
def add_feed(sender, **kwargs):
    instance = sender.objects.latest('id')
    title = None
    if sender in [models.Skill, models.Project]:
        title = instance.name
    elif sender == models.Experience:
        title = instance.company
    elif sender == models.Certification:
        title = instance.cert_name
    elif sender == models.Education:
        title = instance.institute

    link_field = ""
    if hasattr(instance, "link"):
        link_field = instance.link
    elif hasattr(instance, "repository"):
        link_field = instance.repository
    elif hasattr(instance, "live_demo"):
        link_field = instance.live_demo
        
    models.FeedEvent.objects.create(
        source="Heyer.App",

        link=link_field,

        description=f"Added {sender.__name__}{': ' if title else ''}{title}"
    )


# API

class SkillViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          permissions.DjangoModelPermissionsOrAnonReadOnly, ]
    queryset = models.Skill.objects.all()
    serializer_class = serializers.SkillSerializer


class ExperienceViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          permissions.DjangoModelPermissionsOrAnonReadOnly, ]
    queryset = models.Experience.objects.all()
    serializer_class = serializers.ExperienceSerializer


class EducationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          permissions.DjangoModelPermissionsOrAnonReadOnly, ]
    queryset = models.Education.objects.all()
    serializer_class = serializers.EducationSerializer


class CertificationViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          permissions.DjangoModelPermissionsOrAnonReadOnly, ]
    queryset = models.Certification.objects.all()
    serializer_class = serializers.CertificationSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          permissions.DjangoModelPermissionsOrAnonReadOnly, ]
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer


class FeedEventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = models.FeedEvent.objects.all()
    serializer_class = serializers.FeedEventSerializer

class StatusEventViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, ]
    queryset = models.StatusEvent.objects.all()
    serializer_class = serializers.StatusEventSerializer