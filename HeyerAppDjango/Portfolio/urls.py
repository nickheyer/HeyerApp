from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet)
router.register(r'experience', views.ExperienceViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'certifications', views.CertificationViewSet)
router.register(r'projects', views.ProjectViewSet)



urlpatterns = [
    path("", views.Home.as_view(), name="home"),

    path("skills/", views.Skills.as_view(), name="skills"),
    path("skills/create", views.SkillCreate.as_view(), name="skill_create"),
    path("skills/<pk>/delete", views.SkillDelete.as_view(), name="skill_delete"),
    path("skills/<pk>/update", views.SkillUpdate.as_view(), name="skill_update"),

    path("experience/", views.Experience.as_view(), name="experience"),
    path("experience/create", views.ExperienceCreate.as_view(), name="experience_create"),
    path("experience/<pk>/delete", views.ExperienceDelete.as_view(), name="experience_delete"),
    path("experience/<pk>/update", views.ExperienceUpdate.as_view(), name="experience_update"),


    path("education/", views.Education.as_view(), name="education"),
    path("education/create", views.EducationCreate.as_view(), name="education_create"),
    path("education/<pk>/delete", views.EducationDelete.as_view(), name="education_delete"),
    path("education/<pk>/update", views.EducationUpdate.as_view(), name="education_update"),

    path("certifications/", views.Certifications.as_view(), name="certifications"),
    path("certifications/create", views.CertificationCreate.as_view(), name="certification_create"),
    path("certifications/<pk>/delete", views.CertificationDelete.as_view(), name="certification_delete"),
    path("certifications/<pk>/update", views.CertificationUpdate.as_view(), name="certification_update"),

    path("projects/", views.Projects.as_view(), name="projects"),
    path("projects/create", views.ProjectCreate.as_view(), name="project_create"),
    path("projects/<pk>/delete", views.ProjectDelete.as_view(), name="project_delete"),
    path("projects/<pk>/update", views.ProjectUpdate.as_view(), name="project_update"),

    path("accounts/", include("django.contrib.auth.urls"), name="login"),
    path("accounts/logout", views.auth_logout, name="logout"),
    path("accounts/signup", views.UserCreate.as_view(), name="create"),

    path("terminal/", views.Terminal.as_view(), name="terminal"),

    path("resumeapi/", include(router.urls)),
    

]