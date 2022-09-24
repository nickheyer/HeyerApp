from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'skills', views.SkillViewSet)
router.register(r'experience', views.ExperienceViewSet)
router.register(r'education', views.EducationViewSet)
router.register(r'certifications', views.CertificationViewSet)
router.register(r'portfolio', views.PortfolioViewSet)



urlpatterns = [
    path("", views.home, name="home"),
    path("skills/", views.skills, name="skills"),
    path("experience/", views.experience, name="experience"),
    path("education/", views.education, name="education"),
    path("certifications/", views.certifications, name="certifications"),
    path("portfolio/", views.portfolio, name="portfolio"),


    path("accounts/", include("django.contrib.auth.urls"), name="login"),
    path("accounts/logout", views.auth_logout, name="logout"),
    path("accounts/signup", views.auth_create, name="create"),

    path("terminal/", views.terminal, name="terminal"),
    path("resumeapi/", include(router.urls)),
    

]