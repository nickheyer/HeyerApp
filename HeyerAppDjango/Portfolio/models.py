from django.db import models
from django.utils.timezone import now

# Create your models here.
class Skill(models.Model):
    name = models.CharField(verbose_name="Name", max_length = 128, name = "name")
    years = models.IntegerField(verbose_name="Years", name="years")
    link = models.URLField(verbose_name="Link", max_length=128, default= "https://heyer.app")
    image = models.URLField(verbose_name="Image", max_length=128, default="https://via.placeholder.com/60C/O")
    
    class Meta:
        ordering = ["name"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(verbose_name="Company", max_length = 128, name = "company")
    position = models.CharField(verbose_name="Position", max_length = 128, name = "position", default=None)
    description = models.CharField(verbose_name="Description", max_length = 2048, name = "description", default=None)
    start_year = models.CharField(verbose_name="Start Year", max_length = 4, name = "start_year")
    end_year = models.CharField(verbose_name="End Year", max_length = 4, name = "end_year", default="now")
    link = models.URLField(verbose_name="Link", max_length=128, default= "https://heyer.app")
    
    class Meta:
        ordering = ["-start_year"]
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.company

class Education(models.Model):
    institute = models.CharField(verbose_name="Institute", max_length = 128, name = "institute")
    start_year = models.CharField(verbose_name="Start Year", max_length = 4, name = "start_year")
    end_year = models.CharField(verbose_name="End Year", max_length = 4, name = "end_year", default="now")
    link = models.URLField(verbose_name="Link", max_length=128, default= "https://heyer.app")
    
    class Meta:
        ordering = ["-start_year"]
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return self.institute

class Certification(models.Model):
    certifier = models.CharField(verbose_name="Certifier", max_length = 128, name = "certifier")
    year_attained = models.DateField(verbose_name="Year Attained", name = "year_attained", default=now)
    link = models.URLField(verbose_name="Link", max_length=128, default= "https://heyer.app")
    
    class Meta:
        ordering = ["-year_attained"]
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.certifier

class Portfolio(models.Model):
    name = models.CharField(verbose_name="Name", max_length = 128, name = "name")
    year_created = models.DateField(verbose_name="Year Created", name = "year_created", default=now)
    link = models.URLField(verbose_name="Link", max_length=128, default= "https://heyer.app")
    
    class Meta:
        ordering = ["-name"]
        verbose_name = "Portfolio"
        verbose_name_plural = "Portfolio Projects"

    def __str__(self):
        return self.name