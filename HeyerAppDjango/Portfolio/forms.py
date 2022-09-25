from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms.widgets import CheckboxSelectMultiple


from . import models

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class SkillForm(forms.ModelForm):
    class Meta:
        model = models.Skill
        fields = ("__all__")

class ExperienceForm(forms.ModelForm):
    class Meta:
        model = models.Experience
        fields = ("__all__")

class EducationForm(forms.ModelForm):
    class Meta:
        model = models.Education
        fields = ("__all__")

class CertificationForm(forms.ModelForm):
    class Meta:
        model = models.Certification
        fields = ("__all__")

class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = ("__all__")
    def __init__(self, *args, **kwargs):
        
        super(ProjectForm, self).__init__(*args, **kwargs)
        
        self.fields["skill_used"].widget = CheckboxSelectMultiple()
        self.fields["skill_used"].queryset = models.Skill.objects.all()