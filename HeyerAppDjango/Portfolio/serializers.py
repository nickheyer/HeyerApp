from rest_framework import serializers

from . import models

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ('__all__')

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = ('__all__')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = ('__all__')

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Certification
        fields = ('__all__')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('__all__')