from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(
    [
        models.Skill, 
        models.Experience, 
        models.Education, 
        models.Certification,
        models.Project
    ])