from django.db import models
from django.utils.timezone import now


class Skill(models.Model):
    name = models.CharField(verbose_name="Name", max_length = 256, name = "name")
    years = models.IntegerField(verbose_name="Years", name="years")
    link = models.URLField(verbose_name="Link", max_length=256, default= "https://heyer.app")
    image = models.URLField(verbose_name="Image", max_length=256, default="https://via.placeholder.com/60C/O")
    
    class Meta:
        ordering = ["name", "years"]
        verbose_name = "Skill"
        verbose_name_plural = "Skills"

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return '/skills'


class Experience(models.Model):
    company = models.CharField(verbose_name="Company", max_length = 256, name = "company")
    position = models.CharField(verbose_name="Position", max_length = 256, name = "position", default=None)
    description = models.CharField(verbose_name="Description", max_length = 2048, name = "description", default=None)
    start_year = models.CharField(verbose_name="Start Year", max_length = 4, name = "start_year")
    end_year = models.CharField(verbose_name="End Year", max_length = 4, name = "end_year", default="now")
    link = models.URLField(verbose_name="Link", max_length=256, default= "https://heyer.app")
    
    class Meta:
        ordering = ["-pk"]
        verbose_name = "Experience"
        verbose_name_plural = "Experience"

    def __str__(self):
        return self.company

    def get_absolute_url(self):
        return '/experience'

class Education(models.Model):
    institute = models.CharField(verbose_name="Institute", max_length = 256, name = "institute")
    start_year = models.CharField(verbose_name="Start Year", max_length = 4, name = "start_year")
    end_year = models.CharField(verbose_name="End Year", max_length = 4, name = "end_year", default="now")
    link = models.URLField(verbose_name="Link", max_length=256, default= "https://heyer.app")
    image = models.URLField(verbose_name="Image", max_length=256, default="https://via.placeholder.com/60C/O")
    
    class Meta:
        ordering = ["-start_year"]
        verbose_name = "Education"
        verbose_name_plural = "Education"

    def __str__(self):
        return self.institute

    def get_absolute_url(self):
        return '/education'

class Certification(models.Model):
    certifier = models.CharField(verbose_name="Certifier", max_length = 256, name = "certifier")
    cert_name = models.CharField(default="Proficiency Certificate", verbose_name="Certificate Name", max_length = 256, name = "cert_name")
    date_attained = models.DateField(verbose_name="Date Attained", name = "date_attained", default=now)
    link = models.URLField(verbose_name="Link", max_length=256, default= "https://heyer.app")
    
    class Meta:
        ordering = ["-pk"]
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.certifier

    def get_absolute_url(self):
        return '/certifications'

class Project(models.Model):
    name = models.CharField(verbose_name="Name", max_length =256, name = "name")
    description = models.CharField(verbose_name="Description", max_length = 2048, name = "description", default=None)
    year_created = models.DateField(verbose_name="Year Created", name = "year_created", default=now)
    repository = models.URLField(verbose_name="Repository", max_length=256, default=None, name="repository", blank=True)
    live_demo = models.URLField(verbose_name="Live Demo", max_length=256, default=None, name="live_demo", blank=True)
    skills_used = models.ManyToManyField(Skill, verbose_name="Skills Used", name="skill_used",blank=True, default=None, related_name="skills")
    
    class Meta:
        ordering = ["year_created"]
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/projects'

class FeedEvent(models.Model):
    source = models.CharField(verbose_name="Source", max_length =256, name = "source")
    description = models.CharField(verbose_name="Description", max_length = 2048, name = "description", default=None)
    link = models.URLField(verbose_name="Link", max_length=256, default= None, null=True)
    eventdate = models.DateTimeField(verbose_name="Date and Time of Event", name = "eventdate", auto_now_add=True)

    class Meta:
        ordering = ["-eventdate"]
        verbose_name = "Feed Event"
        verbose_name_plural = "Feed Events"

    def __str__(self):
        return self.source

    def get_absolute_url(self):
        return '/'  