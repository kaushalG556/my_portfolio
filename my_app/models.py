from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency = models.PositiveIntegerField(help_text="Enter a value between 0 and 100")

    def __str__(self):
        return self.name

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    company = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    duration = models.CharField(max_length=100)
    description = models.TextField()
    certificate = models.FileField(
        upload_to='experience_certificates/',
        blank=True,
        null=True
    )
    def __str__(self):
        return self.company

class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} on {self.date_sent}"



class Certification(models.Model):
    title = models.CharField(max_length=200)
    platform = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)  # e.g. Jan 2024 – Mar 2024
    image = models.ImageField(upload_to='certificates/')
    certificate_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
