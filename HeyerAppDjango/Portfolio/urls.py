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
    path("terminal/", views.terminal, name="terminal"),
    path("resumeapi/", include(router.urls))

]